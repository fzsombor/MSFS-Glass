function adjustBodyPadding() {
    const navbar = document.querySelector(".navbar");
    const body = document.body;

    if (navbar) {
        // Get the height of the navbar
        const navbarHeight = navbar.offsetHeight;

        // Set body padding dynamically (navbar height + 0.75rem)
        body.style.paddingTop = `calc(${navbarHeight}px + 0.75rem)`;
    }
}

// Run on page load and window resize
window.addEventListener("load", adjustBodyPadding);
window.addEventListener("resize", adjustBodyPadding);

$(document).ready(function () {
    $('.nav-link').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active'); // Deselect if already active
        } else {
            $('.nav-link.active').removeClass('active'); // Remove active from other links
            $(this).addClass('active'); // Activate clicked link
        }
    });
});

$("#elevator-trim-slider")
    .slider({
        min: -30, max: 30, orientation: "vertical"
    })
    .slider("pips", {
        step: "10", first: "pip", last: "pip"
    });

$("#flaps-slider")
    .slider({
        min: -100, max: 0, orientation: "vertical", value: 10
    })
    .slider("pips", {
        step: "50", first: "pip", last: "pip"
    });

$("#rudder-trim-slider")
    .slider({
        min: -50, max: 50, orientation: "horizontal"
    })
    .slider("pips", {
        step: "25", first: "pip", last: "pip"
    });


document.addEventListener("DOMContentLoaded", function () {
    const collapsibles = document.querySelectorAll(".collapse");
    const wrapper = $(".content-wrapper")[0];

    function updateWrapperVisibility() {
        const anyExpanded = Array.from(collapsibles).some(collapse => collapse.classList.contains("show"));
        wrapper.hidden = !anyExpanded;
        if (wrapper.id === "mapContent") {
            wrapper.classList.add("map-content");
        }
    }

    collapsibles.forEach(collapse => {
        collapse.addEventListener("shown.bs.collapse", updateWrapperVisibility);
        collapse.addEventListener("hidden.bs.collapse", updateWrapperVisibility);
    });

    // Initial check in case a collapse is open by default
    updateWrapperVisibility();
    const navbar = document.querySelector(".navbar-nav");
    navbar.addEventListener("wheel", function (event) {
        if (event.deltaY !== 0) {
            event.preventDefault(); // Prevent vertical scrolling
            navbar.scrollLeft += event.deltaY * 0.3; // Scroll horizontally
        }
    }, {passive: false}); // Set passive to false to allow preventDefault()
});

//Sync Frequencies at Startup
syncRadio();

// Fix Map Size

let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);

window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
});

const mapCollapse = $('#collapseMap')[0];
const contentWrapper = $('.content-wrapper')[0];
const contentDiv = $('.content')[0];

if (mapCollapse.classList.contains('show')) {
    contentDiv.classList.add('map-content');
    contentWrapper.classList.add('map-content');
}

mapCollapse.addEventListener('shown.bs.collapse', () => {
    contentWrapper.classList.add('map-content');
    contentDiv.classList.add('map-content');
});

mapCollapse.addEventListener('hidden.bs.collapse', () => {
    contentWrapper.classList.remove('map-content');
    contentDiv.classList.remove('map-content');
});


//Hide Direct Nav/Com and set switch to off
$('#directNAV').hide();
$('#NAVtypeswitch').prop('checked', false);
$('#directCOM').hide();
$('#COMtypeswitch').prop('checked', false);
$('#a320AP').hide();
$('#APtypeswitch').prop('checked', false);


