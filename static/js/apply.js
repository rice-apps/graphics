$(document).ready(function(){
    $('#info').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'none'});
        $('.info').css({'display':'inline-block'});
        $('.designer').css({'display':'none'});
        $('.mini').css({'display':'none'});
    });
    
    $('#lead').click(function(){
        $('.team-lead').css({'display':'inline-block'});
        $('.developer').css({'display':'none'});
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'none'});
        $('.mini').css({'display':'none'});
    });


    $('#designer').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'none'});
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'inline-block'});
        $('.mini').css({'display':'none'});
    });


    $('#developer').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'inline-block'});
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'none'});
        $('.mini').css({'display':'none'});
    });

    $('#mini').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'none'});
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'none'});
        $('.mini').css({'display':'inline-block'});
    });
});