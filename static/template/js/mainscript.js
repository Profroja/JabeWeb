//   TOGGLE FOOTER
// footer-icons-define
		var footer_icon_plus = 'icon-plus-sign';
		var footer_icon_minus = 'icon-minus-sign';
// footer-change-script
var responsiveflagFooter = false;
function accordionFooter(status){
		if(status == 'enable'){
			$('.modules .block h4').on('click', function(){
				$(this).toggleClass('active').parent().find('.toggle_content').stop().slideToggle('medium', function(){
					if($(this).prev().hasClass('active')) {
						$(this).prev().children('i').removeClass(footer_icon_plus).addClass(footer_icon_minus);
					}
					else {
						$(this).prev().children('i').removeClass(footer_icon_minus).addClass(footer_icon_plus);	
					}
				});
			})
			$('.modules').addClass('accordion').find('.toggle_content').slideUp('fast');
		}else{
			$('.modules h4').removeClass('active').off().parent().find('.toggle_content').removeAttr('style').slideDown('fast');
			$('.modules h4 i').removeClass(footer_icon_minus).addClass(footer_icon_plus);
			$('.modules').removeClass('accordion');
		}
	}		
function toDoFooter(){
	   if ($(document).width() <= 992 && responsiveflagFooter == false){
		    accordionFooter('enable');
			responsiveflagFooter = true;		
		}
		else if ($(document).width() >= 992){
			accordionFooter('disable');
	        responsiveflagFooter = false;
		}
}
$(document).ready(toDoFooter);
$(window).resize(toDoFooter);



