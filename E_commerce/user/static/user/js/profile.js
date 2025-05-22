const body = document.getElementById("change");

function change() {
    body.innerHTML = `
    <div class="card-body">
        <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                <h6 class="mb-2 text-primary">Personal Details</h6>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <div class="border-effect"></div>
                    <label for="fullName">Full Name</label>
                    
                    <input type="text" class="form-control" id="fullName" placeholder="Enter full name">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="eMail">Email</label>
                    <div class="border-effect"></div>
                    <input type="email" class="form-control" id="eMail" placeholder="Enter email ID">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="phone">Phone</label>
                    <div class="border-effect"></div>
                    <input type="text" class="form-control" id="phone" placeholder="Enter phone number">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="website">Website URL</label>
                    <div class="border-effect"></div>
                    <input type="url" class="form-control" id="website" placeholder="Website url">
                </div>
            </div>
        </div>
        <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                <h6 class="mt-3 mb-2 text-primary">Address</h6>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="Street">Street</label>
                    <div class="border-effect"></div>
                    <input type="text" class="form-control" id="Street" placeholder="Enter Street">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="ciTy">City</label>
                    <div class="border-effect"></div>
                    <input type="text" class="form-control" id="ciTy" placeholder="Enter City">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="sTate">State</label>
                    <div class="border-effect"></div>
                    <input type="text" class="form-control" id="sTate" placeholder="Enter State">
                </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                <div class="form-group">
                    <label for="zIp">Zip Code</label>
                    <div class="border-effect"></div>
                    <input type="text" class="form-control" id="zIp" placeholder="Zip Code">
                </div>
            </div>
        </div>
        <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                <div class="text-right">
                    <button type="button" id="cancel" name="cancel" class="btn btn-secondary" onclick="cancel()">Cancel</button>
                    <button type="button" id="submit" name="submit" class="btn btn-primary">Update</button>
                </div>
            </div>
        </div>
    </div>
    `;
}

function cancel() {
    body.innerHTML = `
                <div class="card-body">
                        <div class="row gutters">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <h6 class="mb-2 text-primary">Personal Details</h6>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Full Name : {{user.username}}</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Email : {{user.email}}</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Phone : 01836726853</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Website : www.iamshafin121.com</p>
                                </div>
                            </div>
                        </div>
                        <div class="row gutters">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <h6 class="mt-3 mb-2 text-primary">Address</h6>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Street : 35A, cantonment road</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>City : Cumilla</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>State : Chittagong</p>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="form-group">
                                    <p>Zip Code: 3501</p>
                                </div>
                            </div>
                        </div>
                        <div class="row gutters">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <div class="text-right">
                                    <button type="button" id="submit" name="submit"
                                        class="btn btn-primary" onclick="change()">Edit</button>
                                </div>
                            </div>
                        </div>
                    </div>
    `;
}