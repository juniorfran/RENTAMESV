<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Car Rental</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
        <link href="font-awesome/css/all.min.css" rel="stylesheet" type="text/css"/>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
        <link href="css/slick.css" rel="stylesheet" type="text/css"/>
        <link href="css/slick-theme.css" rel="stylesheet" type="text/css"/>
        <link href="css/datepicker.css" rel="stylesheet" type="text/css"/> 
        <link href="css/style.css" rel="stylesheet" type="text/css"/>
        <link href="css/mobyle.css" rel="stylesheet" type="text/css"/>
        <link href="css/animate.min.css" rel="stylesheet" type="text/css"/>

        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Rubik&display=swap" rel="stylesheet">


    </head>
    <body>
        <!-- Topbar Start -->
        <div class="topbar">
            <div class="container-fluid">
                <div class="container">
                    <div class="row">
                        <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12">
                            <div class="topbar-left">
                                <a><i class="fa fa-phone-alt"></i>+012-345-6789</a>
                                <span class="text-body">|</span>
                                <a><i class="fa fa-envelope mr-2"></i>rental@example.com</a>
                            </div>
                        </div>
                        <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12">
                            <div class="topbar-right">
                                <a class="px-3" href="">
                                    <i class="fab fa-facebook-f"></i>
                                </a>
                                <a class="px-3" href="">
                                    <i class="fab fa-twitter"></i>
                                </a>
                                <a class="px-3" href="">
                                    <i class="fab fa-linkedin-in"></i>
                                </a>
                                <a class="px-3" href="">
                                    <i class="fab fa-instagram"></i>
                                </a>
                                <a class="pl-3" href="">
                                    <i class="fab fa-youtube"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>    
            </div>    
        </div>
        <!-- Topbar End -->

        <!-- Navbar Start -->
        <div class="container-fluid position-relative  nav-bar">
            <div class="position-relative px-lg-5" style="z-index: 9;">
                <nav class="navbar navbar-expand-lg bg-secondary navbar-dark py-3 py-lg-0 pl-3 pl-lg-5">
                    <div class="container">
                        <a href="index.html">
                            <img src="image/logo.png" alt="football" height="70">
                        </a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarCollapse">
                            <ul class="navbar-nav mx-auto py-0">
                                <li><a href="index.html" class="nav-item nav-link active">Home</a></li>
                                <li><a href="about.html" class="nav-item nav-link">About</a></li>
                                <li class="nav-item dropdown">
                                    <a href="#" id="menu" data-bs-toggle="dropdown" class="nav-link dropdown-toggle" data-bs-display="static">Cars</a>
                                    <ul class="dropdown-menu">
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Economy</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Compact</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Full Size</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Estate</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Minivan</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">SUV</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Luxury</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Electric</a>
                                        </li>
                                        <li class="dropdown-submenu">
                                            <a href="category.html" class="dropdown-item">Cargo</a>
                                        </li>
                                    </ul>
                                </li>                            
                                <li><a href="service.html" class="nav-item nav-link">Service</a></li>
                                <li><a href="contact.html" class="nav-item nav-link">Contact</a></li>
                                <li class="nav-item dropdown">
                                    <a href="#" data-bs-toggle="dropdown" class="dropdown-item dropdown-toggle nav-item nav-link">My Account</a>
                                    <ul class="dropdown-menu">
                                        <li><a href="my-account.html" class="dropdown-item">My Account</a></li>
                                        <li><a href="booking.html" class="dropdown-item">Booking</a></li>
                                    </ul>
                                </li>        
                            </ul>
                        </div>      
                    </div>    
                </nav>
            </div>
        </div>        
        <!-- Navbar End -->

        <!-- Search Start -->
        <div class="search">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <select class="custom-select px-4">
                            <option selected>Pickup Location</option>
                            <option value="1">Toronto Airport</option>
                            <option value="2">Birmingham</option>
                            <option value="3">Cardiff</option>
                            <option value="4">Coventry</option>
                            <option value="5">Edinburgh</option>
                            <option value="6">Leeds</option>
                            <option value="7">Liverpool</option>
                            <option value="8">Leicester</option>
                            <option value="9">London</option>
                            <option value="10">London City</option>
                            <option value="11">London Gatwick</option>
                            <option value="12">London Heathrow</option>
                            <option value="13">London Luton</option>
                            <option value="14">London Stansted</option>
                            <option value="15">Manchester</option>
                            <option value="16">Nottingham</option>
                            <option value="17">Sheffield</option>
                            <option value="18">Sunderland</option>
                            <option value="19">Southampton</option>
                            <option value="20">Tottenham</option>
                        </select>
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <select class="custom-select px-4">
                            <option selected>Drop Location</option>
                            <option value="1">Birmingham</option>
                            <option value="2">Bristol</option>
                            <option value="3">Cardiff</option>
                            <option value="4">Coventry</option>
                            <option value="5">Edinburgh</option>
                            <option value="6">Leeds</option>
                            <option value="7">Liverpool</option>
                            <option value="8">Leicester</option>
                            <option value="9">London</option>
                            <option value="10">London City</option>
                            <option value="11">London Gatwick</option>
                            <option value="12">London Heathrow</option>
                            <option value="13">London Luton</option>
                            <option value="14">London Stansted</option>
                            <option value="15">Manchester</option>
                            <option value="16">Nottingham</option>
                            <option value="17">Sheffield</option>
                            <option value="18">Sunderland</option>
                            <option value="19">Southampton</option>
                            <option value="20">Tottenham</option>
                        </select>
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <input name="check-in" type="text" class="form-control" id="inputCheckIn" placeholder="Pickup Date">
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <select class="custom-select px-4">
                            <option selected>Drop Off Time</option>
                            <option value="00:30" >12:30 AM</option>
                            <option value="01:00" >01:00 AM</option>
                            <option value="01:30" >01:30 AM</option>
                            <option value="02:00" >02:00 AM</option>
                            <option value="02:30" >02:30 AM</option>
                            <option value="03:00" >03:00 AM</option>
                            <option value="03:30" >03:30 AM</option>
                            <option value="04:00" >04:00 AM</option>
                            <option value="04:30" >04:30 AM</option>
                            <option value="05:00" >05:00 AM</option>
                            <option value="05:30" >05:30 AM</option>
                            <option value="06:00" >06:00 AM</option>
                            <option value="06:30" >06:30 AM</option>
                            <option value="07:00" >07:00 AM</option>
                            <option value="07:30" >07:30 AM</option>
                            <option value="08:00" >08:00 AM</option>
                            <option value="08:30" >08:30 AM</option>
                            <option value="09:00" >09:00 AM</option>
                            <option value="09:30" >09:30 AM</option>
                            <option value="10:00" >10:00 AM</option>
                            <option value="10:30" >10:30 AM</option>
                            <option value="11:00" >11:00 AM</option>
                            <option value="11:30" >11:30 AM</option>
                            <option value="12:00" >12:00 PM</option>
                            <option value="12:30" >12:30 PM</option>
                            <option value="13:00" >01:00 PM</option>
                            <option value="13:30" >01:30 PM</option>
                            <option value="14:00" >02:00 PM</option>
                            <option value="14:30" >02:30 PM</option>
                            <option value="15:00" >03:00 PM</option>
                            <option value="15:30" >03:30 PM</option>
                            <option value="16:00" >04:00 PM</option>
                            <option value="16:30" >04:30 PM</option>
                            <option value="17:00" >05:00 PM</option>
                            <option value="17:30" >05:30 PM</option>
                            <option value="18:00" >06:00 PM</option>
                            <option value="18:30" >06:30 PM</option>
                            <option value="19:00" >07:00 PM</option>
                            <option value="19:30" >07:30 PM</option>
                            <option value="20:00" >08:00 PM</option>
                            <option value="20:30" >08:30 PM</option>
                            <option value="21:00" >09:00 PM</option>
                            <option value="21:30" >09:30 PM</option>
                            <option value="22:00" >10:00 PM</option>
                            <option value="22:30" >10:30 PM</option>
                            <option value="23:00" >11:00 PM</option>
                        </select>
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <select class="custom-select px-4">
                            <option selected>Select A Car</option>
                            <option value="1">Economy</option>
                            <option value="2">Compact</option>
                            <option value="3">Full Size</option>
                            <option value="4">Estate</option>
                            <option value="5">Minivan</option>
                            <option value="6">SUV</option>
                            <option value="7">Luxury</option>
                            <option value="8">Electric</option>
                            <option value="9">Cargo</option>
                        </select>
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-6 col-sm-12">
                        <button class="btn btn-primary btn-block" type="submit" style="height: 50px;">Search</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Search End -->
        
        
        <div class="contact">
            <div class="container-fluid">
                <div class="container">
                    <div class="row">
                        <div class="col-xxl-12 col-xl-12 col-lg-12 col-md-12 col-sm-12">
                            <div class="message">
								<?php $name = $_POST['name'];
									$email = $_POST['email'];
									$message = $_POST['message'];
									$formcontent="From: $name \n Message: $message";
									$recipient = "coffeeshop@coffeeshop.lanams.eu";
									$subject = "Contact Form";
									$mailheader = "From: $email \r\n";
									mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
									echo '
									<div class="details-block">
										<div class="sent-tr-blk">
											<div class="send-blk">
												<div class="order-send-content">
													<div class="sent-inner-text">
														<i class="fa fa-check"></i>
														<span>Thank You! </span>
														<h4>Your booking was successfully sent!</h4>
													</div>
													<p>Thank you for booking.Your booking has been successfully submitted. An order confirmation letter has been sent to your email: email@example.ex.</p>
													<p>In case that the letter does not show up in your inbox folder, please check your spam folder, too.</p>
													<p>If you have any questions, please contact us at the indicated telephone numbers,
                                                        or to the specified email
                                                    </p>
												</div>
											</div>
											<div class="warning-blk">
												<div class="warning-text">
													<i class="fas fa-exclamation-triangle"></i>
													<h5>Warning</h5>
													<p>The price for your service is paid when you return your rental car.</p>
												</div>
											</div>
										</div>
									</div>
											';
								?> 
                            </div>
                        </div>
                    </div>      
                </div>    
            </div>
        </div>    


        <!-- Footer Start -->
        <footer>
            <div class="container-fluid">
                <div class="container">
                    <div class="row">
                        <div class="col-xxl-8 col-xl-8 col-lg-8 col-md-8 col-sm-12">
                            <div class="row">
                                <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12">
                                    <div class="footer-container-left">
                                        <h4>Get In Touch</h4>
                                        <div class="contact-info">
                                            <p><i class="fa fa-map-marker"></i>203 Fake St. Mountain View, <br> 11378 New York</p>
                                            <p><i class="fa fa-envelope"></i>rental@example.com</p>
                                            <p><i class="fa fa-phone"></i>+012-345-6789</p>
                                        </div>
                                        <div class="d-flex mt-4">
                                            <a class="btn btn-secondary btn-square rounded-circle me-2" href="#"><i class="fab fa-twitter"></i></a>
                                            <a class="btn btn-secondary btn-square rounded-circle me-2" href="#"><i class="fab fa-facebook-f"></i></a>
                                            <a class="btn btn-secondary btn-square rounded-circle me-2" href="#"><i class="fab fa-linkedin-in"></i></a>
                                            <a class="btn btn-secondary btn-square rounded-circle" href="#"><i class="fab fa-instagram"></i></a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12">
                                    <div class="footer-container-left">
                                        <h4>Quick Links</h4>
                                        <ul>
                                            <li><a href="about.html">About Us</a></li>
                                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                                            <li><a href="terms.html">Terms & Condition</a></li>
                                            <li><a href="contact.html">Contact</a></li>
                                            <li><a href="category.html">Car Fleet</a></li>
                                        </ul>     
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-4 col-sm-12">
                            <div class="footer-container-right">
                                <h4>Newsletter</h4>
                                <h6>Subscribe Our Newsletter</h6>
                                <form action="#">
                                    <div class="input-group">
                                        <input type="text" class="form-control border-white p-3" placeholder="Your Email">
                                        <button class="btn btn-primary btn-signup">Sign Up</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <div class="footer-bottom">
            <div class="container">
                <div class="row">
                    <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12 copyright">
                        <p>Copyright &copy;
                            <script>document.write(new Date().getFullYear());</script>
                            <a>Car Rental</a>. All Rights Reserved</p>
                    </div>

                    <div class="col-xxl-6 col-xl-6 col-lg-6 col-md-6 col-sm-12 template-by">				
                        <p>Designed By </p>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->


        <script src="jquery/jquery-3.6.0.min.js"></script>
        <script src="js/scroll.js"></script>
        <script src="js/slick.js"></script>
        <script src="bootstrap/js/bootstrap.bundle.js"></script>
        <script src="js/main.js"></script>
        <script src="js/datepicker.min.js"></script>
        <script src="js/datecar.js"></script>
    </body>
</html>