//fixed-nav
$(document).on("scroll",function(){
	if($(document).scrollTop()>20){ 
		$("header").removeClass("large").addClass("small");
	}
	else{
		$("header").removeClass("small").addClass("large");
	}
});


//search
 $(function(){
     $(".attr-nav").each(function(){  
                $(".search", this).on("click", function(e){
                    e.preventDefault();
                    $(".top-search").slideToggle();
                });
            });
            $(".input-group-addon.close-search").on("click", function(){
                $(".top-search").slideUp();
            })
  })


$(function(){
$(document).ready(function() {
		//Horizontal Tab
	    $('#parentHorizontalTab01').easyResponsiveTabs({
	    	type: 'default', //Types: default, vertical, accordion
	        width: 'auto', //auto or any width like 600px
	        fit: true, // 100% fit in a container
	        tabidentify: 'hor_1', // The tab groups identifier
	        activate: function(event) { // Callback function if tab is switched
	        	var $tab = $(this);
	            var $info = $('#nested-tabInfo');
	            var $name = $('span', $info);
	            $name.text($tab.text());
	            $info.show();
	        	}
	    	});

		});
});

//back-top
$(function(){
	$(window).scroll(function(){
		var _top = $(window).scrollTop();
		if(_top>300){
			$('.back_top').fadeIn(600);
		}else{
			$('.back_top').fadeOut(600);
		}
	});
	$(".back_top").click(function(){
		$("html,body").animate({scrollTop:0},500);
	});
});

// fixed service
$(function() {
	$(".online_section").hover(function() {
		$(".online_section").css("right", "0");
		$(".online_section .online_code").css('height', '160px');
	}, function() {
		$(".online_section").css("right", "-220px");
		$(".online_section .online_code").css('height', '40px');
	});
});

$(function() {
	$(".tcon").hover(function() {
		$(this).children(".tcon a").css("left", "34px");
	}, function() {
		$(this).children(".tcon a").css("left", "-200px");
	});
});


//fixed inquiry
$(document).ready(function(){

    $("#floatShow").bind("click",function(){
	
        $("#onlineService").animate({
            height:"show", 
            opacity:"show"
        }, "normal" ,function(){
            $("#onlineService").show();
        });
		
        $("#floatShow").attr("style","display:none");
        $("#floatHide").attr("style","display:block");
		
        return false;
    });
	
    $("#floatHide").bind("click",function(){
	
        $("#onlineService").animate({
            height:"hide", 
            opacity:"hide"
        }, "normal" ,function(){
            $("#onlineService").hide();
        });
		
        $("#floatShow").attr("style","display:block");
        $("#floatHide").attr("style","display:none");
		
        return false;
    });
  
});

$(function(){
	$('.autoplay2').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 2,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:true,
		responsive: [
		{
		  breakpoint:992,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		},
		
	]
	})
})


$(function(){
	$('.autoplay1').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 1,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:true,
		dots:true,
		arrows:false,
	})
})
$(function(){
	$('.autoplay3_1').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:false,
		responsive: [
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		}
	]
	})
})

$(function(){
	$('.autoplay3').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:false,
		responsive: [
		{
		  breakpoint: 992,
		  settings: {
		    slidesToShow:2,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
			}
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		}
	]
	})
})

$(function(){
	$('.autoplay4').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 4,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:false,
		responsive: [
		{
		  breakpoint: 1260,
		  settings: {
		    slidesToShow:3,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
			}
		},
		{
		  breakpoint: 992,
		  settings: {
		    slidesToShow:3,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
			}
		},
		{
		  breakpoint: 768,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		},
		{
		  breakpoint: 400,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		}
	]
	})
})


$(function(){
	$('.autoplay4_1').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 4,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		dots:true,
		pauseOnHover:false,
		responsive: [
		{
		  breakpoint: 992,
		  settings: {
		    slidesToShow:3,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
			dots:true,
			}
		},
		{
		  breakpoint: 768,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
			dots:true,
		  }
		},
		{
		  breakpoint: 400,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
			dots:true,
		  }
		}
	]
	})
})

$(function(){
	$('.autoplay5').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 5,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:true,
		responsive: [
		{
		  breakpoint: 992,
		  settings: {
		    slidesToShow:4,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
			}
		},
		{
		  breakpoint: 768,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
		  }
		}
	]
	})
})


$(function(){
	$('.autoplay6').slick({
		infinite: true,
		speed: 1500,
		slidesToShow: 6,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed:3000,
		pauseOnHover:true,
		dots:false,
		responsive: [
		{
		  breakpoint: 992,
		  settings: {
		    slidesToShow:4,
		    slidesToScroll: 1,
		    autoplay: true,
		    autoplaySpeed:3000,
	        infinite: true,
		    dots:false,
			}
		},
		{
		  breakpoint: 768,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
			dots:false,
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 1,
			autoplay: true,
			autoplaySpeed:3000,
			dots:false,
		  }
		}
	]
	})
})

//faq
var action = 'click';
var speed = "500";

//Document.Ready
$(document).ready(function(){
  //Question handler
$('li.question').on(action, function(){
  //gets next element
  //opens .a of selected question
$(this).next().slideToggle(speed)
    //selects all other answers and slides up any open answer
    .siblings('li.answer').slideUp();
  
  //Grab img from clicked question
var img = $(this).children('div.column');
  //Remove Rotate class from all images except the active
  $('div.column').not(img).removeClass('rotate');
  //toggle rotate class
  img.toggleClass('rotate');

});//End on click
});//End Ready


//select
$(function(){
    $(".select").each(function(){
        var s=$(this);
        var z=parseInt(s.css("z-index"));
        var dt=$(this).children("dt");
        var dd=$(this).children("dd");
        var _show=function(){dd.slideDown(200);dt.addClass("cur");dd.addClass("open");s.css("z-index",z+1);};   //展开效果
        var _hide=function(){dd.slideUp(200);dt.removeClass("cur");dd.removeClass("open");s.css("z-index",z);};    //关闭效果
        dt.click(function(){dd.is(":hidden")?_show():_hide();});
        dd.find("a").click(function(){dt.html($(this).html());_hide();});     //选择效果（如需要传值，可自定义参数，在此处返回对应的“value”值 ）
        $("body").click(function(i){ !$(i.target).parents(".select").first().is(s) ? _hide():"";});
    })
})


$(function(){
	$('.center03').slick({
	  centerMode: true,
	  centerPadding: '0',
	  slidesToShow: 3,
  arrows:false,
	  responsive: [
		{
		  breakpoint: 768,
		  settings: {
			centerMode: true,
			centerPadding: '0',
			slidesToShow:1,
		  }
		},
		{
		  breakpoint:600,
		  settings: {
			centerMode: true,
			centerPadding: '0',
			slidesToShow:1,
	  }
		}
	  ]
	})
})

/*service*/
$(function(){
	$(".service ul li").hover(function(){
		$(this).find(".sidebox").stop().animate({"width":"260px"},100).css({"opacity":"1","filter":"Alpha(opacity=100)","background":"#292929"})	
	},function(){
		$(this).find(".sidebox").stop().animate({"width":"48px"},100).css({"opacity":"1","filter":"Alpha(opacity=100)","background":"#292929"})	
	});
});


$(function($) {
          var $nav = $('#main-nav');
          var $toggle = $('.toggle');
          var defaultData = {
            maxWidth: false,
            customToggle: $toggle,
            levelTitles: true
          };

          // we'll store our temp stuff here
          var $clone = null;
          var data = {};

          // calling like this only for demo purposes

          const initNav = function(conf) {
            if ($clone) {
              // clear previous instance
              $clone.remove();
            }

            // remove old toggle click event
            $toggle.off('click');

            // make new copy
            $clone = $nav.clone();

            // remember data
            $.extend(data, conf)

            // call the plugin
            $clone.hcMobileNav($.extend({}, defaultData, data));
          }

          // run first demo
          initNav({});

          $('.actions').find('a').on('click', function(e) {
            e.preventDefault();

            var $this = $(this).addClass('active');
            var $siblings = $this.parent().siblings().children('a').removeClass('active');

            initNav(eval('(' + $this.data('demo') + ')'));
          });
        });


$(function(){  
  $('.main-more a[href*=#],area[href*=#]').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var $target = $(this.hash);
      $target = $target.length && $target || $('[name=' + this.hash.slice(1) + ']');
      if ($target.length) {
        var targetOffset = $target.offset().top;
        $('html,body').animate({
          scrollTop: targetOffset
        },
        1000);
        return false;
      }
    }
  });
})