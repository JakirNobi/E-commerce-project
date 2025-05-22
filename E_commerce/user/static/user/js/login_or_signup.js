// let container = document.getElementById('container')

// // Existing toggle functionality
function toggle() {
    const container = document.getElementById('container');
    container.classList.toggle('sign-in');
    container.classList.toggle('sign-up');
}


// toggle = () => {
// 	container.classList.toggle('sign-in')
// 	container.classList.toggle('sign-up')
// }

setTimeout(() => {
	container.classList.add('sign-in')
}, 200)