$(document).ready(function(){

    $('#designer').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'none'});
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'inline-block'});
        $('#designer').css({'background-color':'rgb(0,66,113)','color':'white'})
        $('#developer').css({'background-color':'#ddd','color':'#333'})
        $('.mini').css({'display':'none'});
    });


    $('#developer').click(function(){
        $('.team-lead').css({'display':'none'});
        $('.developer').css({'display':'inline-block'});
        $('#developer').css({'background-color':'rgb(0,66,113)','color':'white'})
        $('#designer').css({'background-color':'#ddd','color':'#333'})
        $('.info').css({'display':'none'});
        $('.designer').css({'display':'none'});
        $('.mini').css({'display':'none'});
    });

});