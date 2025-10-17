var $ = jQuery;

$(document).ready(function () {
    $('.equal_height').matchHeight();
    $('.equal_height_inner').matchHeight();

    // Activate sal.js animations
    sal({
        threshold: 0.01,
        once: true, // Ensure animations trigger only once
    });

    // Initialize Slick slider
    $('.slick-a').slick({
        dots: true,
        infinite: true,
        arrows: false,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 4000,
        fade: true,
        cssEase: 'linear',
        prevArrow: '<button class="slide-arrow prev-arrow"><i class="fa-solid fa-angle-left"></i></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><i class="fa-solid fa-angle-right"></i></button>'
    });
    $('.slick-b').slick({
        dots: false,
        infinite: true,
        arrows: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 4000,
        fade: true,
        cssEase: 'linear',
        prevArrow: '<button class="slide-arrow prev-arrow"><i class="icon-arrow-left-line"></i></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><i class="icon-arrow-right-line-right"></i></button>'
    });

    $('.slick-c').slick({
        dots: true,
                infinite: true,
                arrows: true,
                dots: false,
                speed: 500,
                slidesToShow: 3,
                slidesToScroll: 1,
                autoplay: true,
                autoplaySpeed: 3000,
                prevArrow: '<button class="slide-arrow prev-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-left"></i></div></button>',
        nextArrow: '<button class="slide-arrow next-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-right" ></i></div></button>',
                responsive: [
                    {
                        breakpoint: 992,
                        settings: {
                            slidesToShow: 2,
                            slidesToScroll: 2
                        }
                    },
                    {
                        breakpoint: 500,
                        settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1
                        }
                    }
                ]
            });
$('.slick-d').slick({
    dots: true,
    infinite: true,
    arrows: false,
    speed: 600,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    swipe: true,
    swipeToSlide: true,
    prevArrow: '<button class="slide-arrow prev-arrow"><div class="slick-icon"><i class="bx bx-chevron-left"></i></div></button>',
        nextArrow: '<button class="slide-arrow next-arrow"><div class="slick-icon"><i class="bx bx-chevron-right" ></i></div></button>',
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]
});
$('.slick-e').slick({
    dots: false,
    infinite: true,
    arrows: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    swipe: true,
    swipeToSlide: true,
    prevArrow: '<button class="slide-arrow prev-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-left"></i></div></button>',
        nextArrow: '<button class="slide-arrow next-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-right" ></i></div></button>',
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }
    ]
});
$('.slick-f').slick({
    dots: false,
    infinite: true,
    arrows: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    swipe: true,
    swipeToSlide: true,
    pauseOnHover: true,
    prevArrow: '<button class="slide-arrow prev-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-left"></i></div></button>',
        nextArrow: '<button class="slide-arrow next-arrow country-arrow"><div class="slick-icon"><i class="bx bx-chevron-right" ></i></div></button>',
    responsive: [
        {
            breakpoint: 1200,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }
    ]
});


});

//activating sal animation
sal();


//js for the menutoggleMenu
//const menu = document.querySelector(".menu");
const menuInner = menu.querySelector(".menu__inner");
const menuArrow = menu.querySelector(".menu__arrow");
const menuTitle = menu.querySelector(".menu__title");
const burger = document.querySelector(".burger");
const overlay = document.querySelector(".overlay");
const dismiss = document.querySelector("#menu_dismiss");
const body = document.body;


// Navbar Menu Toggle Function
function toggleMenu() {
  menu.classList.add("is-active");
  overlay.classList.add("is-active");
    body.classList.add("open-menu");
    body.style.overflow = 'hidden';
}

//closing submenu in mobile
dismiss.addEventListener ("click", ()=> {
  menu.classList.remove("is-active");
  body.classList.remove("open-menu");
  overlay.classList.remove("is-active");
      body.style.overflow = 'auto';

}) 


// Show Mobile Submenu Function
function showSubMenu(children) {
  subMenu = children.querySelector(".submenu");
  subMenu.classList.add("is-active");
  subMenu.style.animation = "slideLeft 0.35s ease forwards";
  const menuTitle = children.querySelector("i").parentNode.childNodes[0]
    .textContent;
  menu.querySelector(".menu__title").textContent = menuTitle;
  menu.querySelector(".menu__header").classList.add("is-active");
}

// Hide Mobile Submenu Function
function hideSubMenu() {
  subMenu.style.animation = "slideRight 0.35s ease forwards";
  setTimeout(() => {
    subMenu.classList.remove("is-active");
  }, 300);

  menu.querySelector(".menu__title").textContent = "";
  menu.querySelector(".menu__header").classList.remove("is-active");
}

// Toggle Mobile Submenu Function
function toggleSubMenu(e) {
  if (!menu.classList.contains("is-active")) {
    return;
  }
  if (e.target.closest(".menu__dropdown")) {
    const children = e.target.closest(".menu__dropdown");
    showSubMenu(children);
  }
}

// Fixed Navbar Menu on Window Resize
window.addEventListener("resize", () => {
  if (window.innerWidth >= 768) {
    if (menu.classList.contains("is-active")) {
      toggleMenu();
    }
  }
});

//js for header boz-shadow wheb scrolls
window.addEventListener("scroll", function () {
  const header = document.getElementById("header");

  if (window.scrollY > 0) {
    header.style.boxShadow = "none";
  } else {
    header.style.boxShadow = "none";
  }
});


// Initialize All Event Listeners
burger.addEventListener("click", toggleMenu);
// overlay.addEventListener("click", toggleMenu);
menuArrow.addEventListener("click", hideSubMenu);
menuTitle.addEventListener("click", hideSubMenu);
menuInner.addEventListener("click", toggleSubMenu);


//jquery for the equal height ends
 
 

//limiting words
document.addEventListener("DOMContentLoaded", () => {
  const wordLimit = 5;

  document.querySelectorAll(".limit-words-5").forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    if (words.length > wordLimit) {
      el.textContent = words.slice(0, wordLimit).join(" ");
    }
  });
});

//limiting words
document.addEventListener("DOMContentLoaded", () => {
  const wordLimit = 6;

  document.querySelectorAll(".limit-words-7").forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    if (words.length > wordLimit) {
      el.textContent = words.slice(0, wordLimit).join(" ") + " ...";
    }
  });
});


//dynamic checked for input for opening first tab opened
document.addEventListener("DOMContentLoaded", function () {
  const firstTabInput = document.querySelector(".tabs .tab input[type='checkbox']");
  if (firstTabInput) {
    firstTabInput.classList.add("checked");
  }
});


/** Testimonials Video JS Start **/

$(document).ready(function () {
  $('.play-icon').on('click', function () {
    const videoId = $(this).data('video-id'); // could be YouTube ID or full video URL
    const type = $(this).data('type'); // 'youtube' or 'uploaded'
    let embedUrl = '';

    if (type === 'youtube') {
      embedUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
    } else {
      // For uploaded video files, directly embed the file
      embedUrl = videoId; // already a full path like /storage/videos/filename.mp4
    }

    $('#yt-video')
      .attr('src', embedUrl)
      .attr('allow', 'autoplay'); // Ensure autoplay permission

    $('.video-modal').fadeIn();
  });

  // Close modal and stop video
  $('.close-btn, .modal-overlay').on('click', function () {
    $('#yt-video').attr('src', '');
    $('.video-modal').fadeOut();
  });
});

/** Testimonials Video JS End **/


/**js for whatsapp chat **/
!(function (a) {
  var t, p;
  a(document).ready(function () {
    function o(a) {
      for (
        var t = a + "=", p = document.cookie.split(";"), o = 0;
        o < p.length;
        o++
      ) {
        for (var n = p[o]; " " == n.charAt(0); ) n = n.substring(1);
        if (0 == n.indexOf(t)) return n.substring(t.length, n.length);
      }
      return "";
    }
    a(".wa__btn_popup").on("click", function () {
      a(".wa__popup_chat_box").hasClass("wa__active")
        ? (a(".wa__popup_chat_box").removeClass("wa__active"),
          a(".wa__btn_popup").removeClass("wa__active"),
          clearTimeout(p),
          a(".wa__popup_chat_box").hasClass("wa__lauch") &&
            (t = setTimeout(function () {
              a(".wa__popup_chat_box").removeClass("wa__pending"),
                a(".wa__popup_chat_box").removeClass("wa__lauch");
            }, 400)))
        : (a(".wa__popup_chat_box").addClass("wa__pending"),
          a(".wa__popup_chat_box").addClass("wa__active"),
          a(".wa__btn_popup").addClass("wa__active"),
          clearTimeout(t),
          a(".wa__popup_chat_box").hasClass("wa__lauch") ||
            (p = setTimeout(function () {
              a(".wa__popup_chat_box").addClass("wa__lauch");
            }, 100)));
    }),
      a("#nta-wa-gdpr").change(function () {
        if (this.checked) {
          var t, p;
          (t = new Date()).setTime(t.getTime() + 2592e6),
            (p = "expires=" + t.toUTCString()),
            (document.cookie = "nta-wa-gdpr=accept;" + p + ";path=/"),
            "" != o("nta-wa-gdpr") &&
              (a(".nta-wa-gdpr").hide(500),
              a(".wa__popup_content_item").each(function () {
                a(this).removeClass("pointer-disable"),
                  a(".wa__popup_content_list").off("click");
              }));
        }
      }),
      "" != o("nta-wa-gdpr")
        ? a(".wa__popup_content_list").off("click")
        : a(".wa__popup_content_list").click(function () {
            a(".nta-wa-gdpr")
              .delay(500)
              .css({ background: "red", color: "#fff" });
          });
  });
})(jQuery);
// close out script


/**added is here */
/* Whatsapp Chat Widget by www.bloggermix.com */
$(document).on("click", "#send-it", function() {
  var a = document.getElementById("chat-input");
  if ("" != a.value) {
    var b = $("#get-number").text(),
      c = document.getElementById("chat-input").value,
      d = "https://web.whatsapp.com/send",
      e = b,
      f = "&text=" + c;
    if (
      /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
      )
    )
      var d = "whatsapp://send";
    var g = d + "?phone=" + e + f;
    window.open(g, "_blank");
  }
}),


  $(document).on("click", ".informasi", function() {
    (document.getElementById("get-number").innerHTML = $(this)
      .children(".my-number")
      .text()),
      $(".start-chat,.get-new")
        .addClass("show")
        .removeClass("hide"),
      $(".home-chat,.head-home")
        .addClass("hide")
        .removeClass("show"),
      (document.getElementById("get-nama").innerHTML = $(this)
        .children(".info-chat")
        .children(".chat-nama")
        .text()),
      (document.getElementById("get-label").innerHTML = $(this)
        .children(".info-chat")
        .children(".chat-label")
        .text());
  }),
  $(document).on("click", ".close-chat", function() {
    $("#whatsapp-chat")
      .addClass("hide")
      .removeClass("show");
  }),
  $(document).on("click", ".blantershow-chat", function() {
    $("#whatsapp-chat")
      .addClass("show")
      .removeClass("hide");
  });

$(document).on("keydown", "#chat-input", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault(); // Prevent newline
    $("#send-it").click(); // Trigger click to send message
  }
});
//   //script for whatsapp chat time
//   function formatTime(date) {
//     let hours = date.getHours();
//     let minutes = date.getMinutes();
//     // Optional: Convert to 12-hour format
//     hours = hours % 12 || 12;
//     minutes = minutes < 10 ? '0' + minutes : minutes;
//     return `${hours}:${minutes}`;
//   }

//   // Set current time
//   document.getElementById("whatsappTime").textContent = formatTime(new Date());

//   // Optional: Update every minute
//   setInterval(() => {
//     document.getElementById("whatsappTime").textContent = formatTime(new Date());
//   }, 60000);


//   //js for whatsapp text area
// document.getElementById('chat-input')?.addEventListener('input', function () {
//   this.style.height = 'auto';
//   this.style.height = this.scrollHeight + 'px';
// });

// //js for whatsapp chat ends here


// Check if current page is NOT homepage
if (window.location.pathname !== '/' && window.location.pathname !== '/index.html' && window.pathname !== '' && window.pathname !== '') {
  document.querySelectorAll('a').forEach(link => {
    link.setAttribute('target', '');
  });
}
//js for no blank
document.querySelectorAll('a').forEach(link => {
  if (!link.hasAttribute('data-no-blank')) {
    link.setAttribute('target', '');
  } else {
    link.removeAttribute('target');
  }
});
// Select the second link in the menu
// Array of desired child positions
const positions = [2, 3, 4, 7];

// Loop through each position and set data-no-blank on the <a> inside that <li>
positions.forEach(pos => {
  const link = document.querySelector(`ul.menu__inner li:nth-child(${pos}) a`);
  if (link) {
    link.setAttribute('data-no-blank', '');
  }
});

// Set or remove target based on rules and prevent default navigation
document.querySelectorAll('a').forEach(link => {
  const href = link.getAttribute('href')?.trim(); // Trim to handle whitespace

  // Remove target if:
  // - href is null, undefined, empty, "#", "/", or "default"
  // - OR link has data-no-blank
  if (
    !href || // Covers null, undefined, or empty string
    href === '#' ||
    href === '/' ||
    href === 'default' ||
    link.hasAttribute('data-no-blank')
  ) {
    link.removeAttribute('target');
    // Prevent default navigation for href="" or href="#"
    if (!href || href === '#') {
      link.addEventListener('click', (e) => {
        e.preventDefault(); // Stop navigation to current pathname
      });
    }
  } else {
    link.setAttribute('target', '');
  }
});


//js for lightbox and album gallery
$(document).ready(function() {
  // Lightbox open handler
  $(".image-container img").click(function() {
    var $img = $(this);
    $(".lightbox").fadeIn(300);
$(".lightbox").append(`
  <div class="lightbox-image-container">
    <img src="${$img.attr("src")}" alt="${$img.attr("alt")}" />
  </div>
`);
    // $(".filter").css("background-image", "url(" + $img.attr("src") + ")");
    $("html").css("overflow", "hidden");
    
    // Update arrow visibility
    updateArrows($img);
  });

// Lightbox close handler
$(".lightbox").click(function(e) {
  // If clicked on image, arrows, or close button (or their children), do NOT close
  if (
    $(e.target).is("img") ||
    $(e.target).closest(".arrowr, .arrowl").length > 0
  ) {
    return; // do nothing
  }
  // Otherwise, close the lightbox
  closeLightbox();
});


  // Keyboard navigation
  $(document).keyup(function(e) {
    if (e.keyCode == 27) { // ESC key
      closeLightbox();
    } else if ($(".lightbox").is(":visible")) {
      if (e.keyCode == 39) { // Right arrow
        navigate(1);
      } else if (e.keyCode == 37) { // Left arrow
        navigate(-1);
      }
    }
  });

  // Arrow navigation
  $(".arrowr").click(function() { navigate(1); });
  $(".arrowl").click(function() { navigate(-1); });

  // Helper functions
  function closeLightbox() {
    $(".lightbox").fadeOut(300);
    $(".lightbox img").remove();
    $("html").css("overflow", "auto");
  }

  function navigate(direction) {
    var currentSrc = $(".lightbox img").attr("src");
    var $images = $(".image-container img");
    var currentIndex = $images.index($images.filter("[src$='" + currentSrc + "']"));
    var newIndex = currentIndex + direction;
    
    if (newIndex >= 0 && newIndex < $images.length) {
      var $newImg = $images.eq(newIndex);
      $(".lightbox img").attr({
        src: $newImg.attr("src"),
        alt: $newImg.attr("alt")
      });
    //   $(".filter").css("background-image", "url(" + $newImg.attr("src") + ")");
      updateArrows($newImg);
    }
  }

  function updateArrows($img) {
    $(".arrowr").toggle(!$img.is(":last-child"));
    $(".arrowl").toggle(!$img.is(":first-child"));
  }
});
//js for counsellor tabs
document.querySelectorAll('#locationPills .nav-link').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();

      // Remove active from all pills
      document.querySelectorAll('#locationPills .nav-link').forEach(p => p.classList.remove('active'));

      // Add active to clicked pill
      link.classList.add('active');

      // Sync the select dropdown
      const location = link.getAttribute('data-location');
      const select = document.getElementById('selectInput');
      if (select) {
        select.value = location;
      }

      // Submit the form
      const form = select.closest('form');
      if (form) {
        form.submit();
      }
    });
  });
document.addEventListener('click', function (e) {
  const anchor = e.target.closest('a');
  if (!anchor) return;

  const href = anchor.getAttribute('href');

  if (
    href === '#' || 
    href === '' || 
    href === null
  ) {
    e.preventDefault();
  }
});

// document.addEventListener("DOMContentLoaded", function() {
//     const video = document.querySelector(".banner-video");
    
//     if (video) {
//         // Set volume to 0 (even though muted) to help with autoplay
//         video.volume = 0;
        
//         // Load video first before playing
//         video.load();
        
//         const playAttempt = setInterval(() => {
//             video.play()
//                 .then(() => {
//                     console.log("Playback started");
//                     clearInterval(playAttempt);
//                 })
//                 .catch(error => {
//                     console.warn("Playback attempt failed:", error);
//                 });
//         }, 500);
  //      msnry
//         // Fallback if still not playing after 5 seconds
//         setTimeout(() => {
//             clearInterval(playAttempt);
//         }, 5000);
//     }
// });
// // Add this to your existing script
// function simulateClick() {
//     const clickEvent = new MouseEvent('click', {
//         view: window,
//         bubbles: true,
//         cancelable: true
//     });
//     document.dispatchEvent(clickEvent);
// }

// // Run after a small delay
// setTimeout(simulateClick, 500);




    //script for the bootstrap modal
document.addEventListener("DOMContentLoaded", function () {
    var popupEl = document.getElementById('homepageModal');
    if (!popupEl) return;  

    var popupModal = bootstrap.Modal.getOrCreateInstance(popupEl);

    popupModal.show();

    setTimeout(function () {
        popupModal.hide();
    }, 6000);
});