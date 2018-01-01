	<style>
		/* main menu styles */
		#nav {
		//border-radius:5px; /*some css3*/
		//-moz-border-radius:5px;
		//-webkit-border-radius:5px;
		//box-shadow:0 1px 1px rgba(0,0,0, .5);
		//-moz-box-shadow:0 1px 1px rgba(0,0,0, .5);
		//-webkit-box-shadow:0 1px 1px rgba(0,0,0, .5);
		<?php echo $bg1; ?>;
		width:100%;
		}
		#nav li {
		margin:10px;
		<?php echo $bg2; ?>;
		}
		#nav a {
		font-weight:bold;
		
		padding:0px 0px;
		padding-left:5px;
		padding-right:5px;
		//border-radius:5px; /*some css3*/
		//-moz-border-radius:5px;
		//-webkit-border-radius:5px;
		//text-shadow:0 2px 2px rgba(0,0,0, .7);
		
		}
		 
		/* selected menu element */
		#nav .current a, #nav li:hover > a {
		background:<?php echo $color4; ?>;
		color:<?php echo $color3; ?>;
		//border-top:1px solid <?php echo $color2; ?>;
		 
		//box-shadow:0 2px 2px rgba(0,0,0, .7); /*some css3*/
		//-moz-box-shadow:0 2px 2px rgba(0,0,0, .7);
		//-webkit-box-shadow:0 2px 2px rgba(0,0,0, .7);
		//text-shadow:0 2px 2px rgba(255,255,255, 0.7);
		
		}
		 
		/* sublevels */
		#nav ul li:hover a, #nav li:hover li a {
		
		background-color:<?php echo $color6; ?>;
		//border:none;
		color:<?php echo $color5; ?>;
		
		}
		#nav ul li a:hover {
		background:<?php echo $color8; ?>;
		color:<?php echo $color7; ?>;
		 
		//border-radius:5px; /*some css3*/
		//-moz-border-radius:5px;
		//-webkit-border-radius:5px;
		//text-shadow:0 2px 2px rgba(0,0,0, 0.7);
		}
		 
		#nav ul li:first-child > a {
		//-moz-border-radius-topleft:5px; /*some css3*/
		//-moz-border-radius-topright:5px;
		//-webkit-border-top-left-radius:5px;
		//-webkit-border-top-right-radius:5px;
		}
		#nav ul li:last-child > a {
		//-moz-border-radius-bottomleft:5px; /*some css3*/
		//-moz-border-radius-bottomright:5px;
		//-webkit-border-bottom-left-radius:5px;
		//-webkit-border-bottom-right-radius:5px;
		}
		 
		/* drop down */
		#nav li:hover > ul {
		opacity:1;
		visibility:visible;
		z-index:555;
		}
		#nav ul {
		opacity:0;
		visibility:hidden;
		padding:0;
		width: 200px;
		position:absolute;
		background:<?php echo $color2; ?>;
		border:1px solid <?php echo $color9; ?>;
		 
		//border-radius:5px; /*some css3*/
		//-moz-border-radius:5px;
		//-webkit-border-radius:5px;
		//box-shadow:0 2px 2px rgba(0,0,0, .5);
		//-moz-box-shadow:0 2px 2px rgba(0,0,0, .5);
		//-webkit-box-shadow:0 2px 2px rgba(0,0,0, .5);
		 
		//-moz-transition:opacity .25s linear, visibility .1s linear .1s;
		//-webkit-transition:opacity .25s linear, visibility .1s linear .1s;
		//-o-transition:opacity .25s linear, visibility .1s linear .1s;
		//transition:opacity .25s linear, visibility .1s linear .1s;
		}
		#nav ul li {
		float:none;
		margin:0;
		}
		#nav ul a {
		font-weight:normal;
		//text-shadow:0 2px 2px rgba(255,255,255, 0.7);
		}
		#nav ul ul {
		left:160px;
		top:0px;
		}
		
		.navbar-custom {
		  background-color:<?php echo $color2; ?>;<!-- màu nền -->;
		  
		}
		.navbar-custom .navbar-brand {
		  color: #9d9d9d;
		}
		.navbar-custom .navbar-brand:hover,
		.navbar-custom .navbar-brand:focus {
		  color: #fff;
		  background-color: transparent;
		}
		.navbar-custom .navbar-text {
		  color: #9d9d9d;
		}
		.navbar-custom .navbar-nav > li > a {
		  color:<?php echo $color1; ?>; <!-- màu chữ -->;
		}
		.navbar-custom .navbar-nav > li > a:hover,
		.navbar-custom .navbar-nav > li > a:focus {
		  color:<?php echo $color3; ?>; <!-- màu khi trỏ vào -->;
		  background-color:<?php echo $color4; ?>;
		}
		.navbar-custom .navbar-nav > .active > a,
		.navbar-custom .navbar-nav > .active > a:hover,
		.navbar-custom .navbar-nav > .active > a:focus {
		  color: #fff;
		  background-color: red;
		}
		.navbar-custom .navbar-nav > .disabled > a,
		.navbar-custom .navbar-nav > .disabled > a:hover,
		.navbar-custom .navbar-nav > .disabled > a:focus {
		  color: #444;
		  background-color: transparent;
		}
		.navbar-custom .navbar-toggle {
		  border-color: #333;
		}
		.navbar-custom .navbar-toggle:hover,
		.navbar-custom .navbar-toggle:focus {
		  background-color: #333;
		}
		.navbar-custom .navbar-toggle .icon-bar {
		  background-color: #fff;
		}
		.navbar-custom .navbar-collapse,
		.navbar-custom .navbar-form {
		  border-color: #101010;
		}
		.navbar-custom .navbar-nav > .open > a,
		.navbar-custom .navbar-nav > .open > a:hover,
		.navbar-custom .navbar-nav > .open > a:focus {
		  color: #fff;
		  background-color: #080808;
		}
		@media (max-width: 767px) {
		  .navbar-custom .navbar-nav .open .dropdown-menu > .dropdown-header {
			border-color: #080808;
		  }
		  .navbar-custom .navbar-nav .open .dropdown-menu .divider {
			background-color: #080808;
		  }
		  .navbar-custom .navbar-nav .open .dropdown-menu > li > a {
			color: #9d9d9d;
		  }
		  .navbar-custom .navbar-nav .open .dropdown-menu > li > a:hover,
		  .navbar-custom .navbar-nav .open .dropdown-menu > li > a:focus {
			color: #fff;
			background-color: transparent;
		  }
		  .navbar-custom .navbar-nav .open .dropdown-menu > .active > a,
		  .navbar-custom .navbar-nav .open .dropdown-menu > .active > a:hover,
		  .navbar-custom .navbar-nav .open .dropdown-menu > .active > a:focus {
			color: #fff;
			background-color: #080808;
		  }
		  .navbar-custom .navbar-nav .open .dropdown-menu > .disabled > a,
		  .navbar-custom .navbar-nav .open .dropdown-menu > .disabled > a:hover,
		  .navbar-custom .navbar-nav .open .dropdown-menu > .disabled > a:focus {
			color: #444;
			background-color: transparent;
		  }
		}
		.navbar-custom .navbar-link {
		  color: #9d9d9d;
		}
		.navbar-custom .navbar-link:hover {
		  color: #fff;
		}
		.navbar-custom .btn-link {
		  color: #9d9d9d;
		}
		.navbar-custom .btn-link:hover,
		.navbar-custom .btn-link:focus {
		  color: #fff;
		}
		.navbar-custom .btn-link[disabled]:hover,
		fieldset[disabled] .navbar-custom .btn-link:hover,
		.navbar-custom .btn-link[disabled]:focus,
		fieldset[disabled] .navbar-custom .btn-link:focus {
		  color: #444;
		}
	</style>
	<nav style="margin-top:1px;" class="navbar navbar-custom navbar-static-top">
	  <div class="container">
		<div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="true" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
		<div id="navbar" class="navbar-collapse collapse in" aria-expanded="true">
		  <ul id="nav" class="nav navbar-nav">
			<li><a href="index.php">Trang chủ</a></li>
			<li><a href="index.php">Tải Game</a>
			<ul>
				<li><a href="index.php">Trang chủ</a></li>
				<li><a href="index.php">Tải Game</a>
					<ul>
						<li><a href="index.php">Trang chủ</a></li>
						<li><a href="index.php">Tải Game</a></li>
					</ul>
				
				</li>
			</ul>
			</li>
			<!-- hien thi menu -->
			
					
					
			
		  </ul>
		</div>
	  </div>
	</nav>