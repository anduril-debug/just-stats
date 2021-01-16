import React from 'react';
import './Navbar.css';
import logo from '../assets/logo.png';


function Navbar() {
	return (

		<>
			<nav className="navbar navbar-expand-lg navbar-dark pink">
				<div id="navbar-field" className="container-fluid">
					<div className="col-4">
						<img src={logo} alt="Prem Stats" className="logo" />
					</div>
					<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
						<span className="navbar-toggler-icon"></span>
					</button>
					<div className="collapse navbar-collapse col-8" id="navbarNav">
						<ul className="navbar-nav">
							<li className="nav-item">
								<a className="nav-link" aria-current="page" href="#">Home</a>
							</li>
						</ul>
					</div>
				</div>
			</nav>
		</>
	);
}


export default Navbar;