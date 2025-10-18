(function( window , document ){
    'use strict';
    var hotcss = {};
    (function() {
        var viewportEl = document.querySelector('meta[name="viewport"]'),
            hotcssEl = document.querySelector('meta[name="hotcss"]'),
            dpr = window.devicePixelRatio || 1,
            maxWidth = 640,
            designWidth = 0;
        
        document.documentElement.setAttribute('data-dpr', dpr);
        hotcss.dpr = dpr;
        document.documentElement.setAttribute('max-width', maxWidth);
        hotcss.maxWidth = maxWidth;
        if( designWidth ){
            document.documentElement.setAttribute('design-width', designWidth);
            hotcss.designWidth = designWidth;
        }
    })();
    hotcss.px2rem = function( px , designWidth ){
        if( !designWidth ){
            designWidth = parseInt(hotcss.designWidth , 10);
        }
        return parseInt(px,10)*640/designWidth/20;
    }
    hotcss.rem2px = function( rem , designWidth ){
        if( !designWidth ){
            designWidth = parseInt(hotcss.designWidth , 10);
        }
        return rem*20*designWidth/640;
    }
    hotcss.mresize = function(){
        var innerWidth = document.documentElement.getBoundingClientRect().width || window.innerWidth;
        if( hotcss.maxWidth && (innerWidth/hotcss.dpr > hotcss.maxWidth) ){
            innerWidth = hotcss.maxWidth*hotcss.dpr;
        }
        if( !innerWidth ){ return false;}
        document.documentElement.style.fontSize = ( innerWidth*20/640 ) + 'px';
    };
    hotcss.mresize();
    window.addEventListener( 'resize' , function(){
        clearTimeout( hotcss.tid );
        hotcss.tid = setTimeout( hotcss.mresize , 400 );
    } , false );
    window.addEventListener( 'load' , hotcss.mresize , false );
    setTimeout(function(){
        hotcss.mresize();
    },333)
    window.hotcss = hotcss;
})( window , document );
(function($){
    var mainWit = $(window).width(),
        mainHit = $(window).height(),
        carouselBar = $(".page-header-bar"),
        fixedContact = $(".fixed-contact");
	/*fixed-contact*/
    $(".fixed-contact").hover(function(){
        $(this).addClass("active");
    },function(){
        $(this).removeClass("active");
    });
    $(window).scroll(function() {
        if($(window).width() > 992){
            if ($(this).scrollTop() > mainHit/2 ){
                carouselBar.addClass("active");
                fixedContact.addClass("show");
            } else {
                carouselBar.removeClass("active");
                fixedContact.removeClass("show");
            }
        }
    });
})(jQuery);