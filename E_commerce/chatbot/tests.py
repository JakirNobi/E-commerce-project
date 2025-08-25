from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
from chatbot.models import ChatHistory

class ChatbotViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_chat_view_get(self):
        """Test that the chat view loads correctly"""
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chatbot/chat.html')
    
    def test_chat_view_post_success(self):
        """Test successful chat response"""
        # Mock the database chain response
        with patch('chatbot.views.db_chain') as mock_db_chain:
            mock_db_chain.run.return_value = "Test product information"
            
            response = self.client.post(reverse('chat'), {
                'user_input': 'Tell me about products'
            })
            
            self.assertEqual(response.status_code, 200)
            self.assertJSONEqual(
                str(response.content, encoding='utf8'),
                {'response': 'Test product information'}
            )
            
            # Check that the chat history was saved
            self.assertEqual(ChatHistory.objects.count(), 2)
            user_message = ChatHistory.objects.get(is_user_message=True)
            bot_message = ChatHistory.objects.get(is_user_message=False)
            
            self.assertEqual(user_message.message, 'Tell me about products')
            self.assertEqual(bot_message.message, 'Test product information')
    
    def test_chat_view_post_greeting(self):
        """Test greeting response"""
        response = self.client.post(reverse('chat'), {
            'user_input': 'Hello'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'Hello! How can I assist you with your shopping today?'}
        )
    
    def test_chat_view_post_sensitive_info(self):
        """Test that sensitive information queries are blocked"""
        response = self.client.post(reverse('chat'), {
            'user_input': 'What is my password?'
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'response': 'For privacy reasons, I cannot answer questions about user information.'}
        )
    
    def test_chat_view_post_error_handling(self):
        """Test error handling in chat response"""
        # Mock an exception from the database chain
        with patch('chatbot.views.db_chain') as mock_db_chain:
            mock_db_chain.run.side_effect = Exception("API Error")
            
            response = self.client.post(reverse('chat'), {
                'user_input': 'Tell me about products'
            })
            
            self.assertEqual(response.status_code, 200)
            response_data = str(response.content, encoding='utf8')
            # Check that we get an error response
            self.assertIn('I encountered an issue processing your request', response_data)