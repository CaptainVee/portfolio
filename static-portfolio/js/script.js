

// Define UI variables
const tabContainer = document.querySelector(".about-tabs")
let aboutSection = document.querySelector(".about-section")
const portfolioSection = document.querySelector(".portfolio-section")
var ppclose = document.querySelector(".pp-close")
const navToggler = document.querySelector(".nav-toggler");

// load all event listeners
loadEventListeners()



function loadEventListeners(){
	tabContainer.addEventListener("click", tabEvent);
	ppclose.addEventListener("click", togglePortfolioPopup);
	navToggler.addEventListener("click", navButton);
	document.addEventListener("click", navEvent);
	window.addEventListener("load", pageLoader);
}


//----Page Loader

function pageLoader(){
	document.querySelector(".main").classList.remove("hidden")
	document.querySelector(".home-section").classList.add("active")
	document.querySelector(".page-loader").classList.add("fade-out")
	setTimeout(()=>{
		document.querySelector(".page-loader").style.display = "none";
	}, 600)
}

//-----Nav toggle button
function navButton() {
	document.querySelector("section.active").classList.toggle("fade-out");
	document.querySelector(".header").classList.toggle("active");
	document.body.classList.toggle("hide-scrolling")
}

//-----Nav Pages Toggle
function navEvent(e){
	if(e.target.classList.contains("link-item") && e.target.hash !== ""){
		//activate the overlay to prevent multiple clicks
		document.querySelector(".overlay").classList.add("active")
		navToggler.classList.add("hide")
		if(e.target.classList.contains("nav-item")){
			document.querySelector(".header").classList.toggle("active");
		}
		else{
			document.querySelector("section.active").classList.toggle("fade-out");
			document.body.classList.add("hide-scrolling")
		}
		setTimeout(()=>{
			document.querySelector('section.active').classList.remove("active", "fade-out");
			document.querySelector(e.target.hash).classList.add("active");
			window.scrollTo(0,0);
			document.body.classList.remove("hide-scrolling")
			navToggler.classList.remove("hide")
			document.querySelector(".overlay").classList.remove("active")
		}, 500);
	}
}


//------About tabs (experience and Education)
function tabEvent(e){
 	if(e.target.classList.contains("tab-item") && !e.target.classList.contains("active")){
		tabContainer.querySelector(".active").classList.remove("active");
		e.target.classList.add("active");
		const target = e.target.getAttribute("data-target");
		aboutSection.querySelector(".tab-content.active").classList.remove("active");
		aboutSection.querySelector(target).classList.add("active");
}}





//----Portforlio list and detail view toggle


//opens portfolio detail view
function portfolioItemDetails(portfolioItem){
	document.querySelector(".pp-thumbnail img").src= portfolioItem.querySelector(".portfolio-item-thumbnail img").src;
    document.querySelector(".pp-header h3").innerHTML = portfolioItem.querySelector(".portfolio-item-title").innerHTML;
    document.querySelector(".pp-body").innerHTML = portfolioItem.querySelector(".portfolio-item-details").innerHTML;
}


function togglePortfolioPopup() {
	document.querySelector(".portfolio-popup").classList.toggle("open");
	document.body.classList.toggle("hide-scrolling");
	document.querySelector(".main").classList.toggle("fade-out");

}

// close portfolio detail view when top button is clicked
portfolioSection.addEventListener("click", (e)=>{
	if(e.target.classList.contains("view-project-btn")){
		togglePortfolioPopup();
		document.querySelector(".portfolio-popup").scrollTo(0,0);
		portfolioItemDetails(e.target.parentElement);
	};
})

// close portfolio details when clicked outside the card
document.addEventListener("click", (e)=>{
    if(e.target.classList.contains("pp-inner")){
    	togglePortfolioPopup();
    };
})


