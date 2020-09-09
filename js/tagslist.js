/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(document).ready(function () {
    //find the list of tags practiced
    var elementlist = $(".practice * ");
    //load the external html  --- This portion of code need to run on server
    var $newdiv = $("<div id='side'></div>");
    $("body").prepend($newdiv);
    $("#side").load("HTMLelements.html", function () {

        //highlisht tags
        $.each(elementlist, function (i, v) {
            var tn = v.tagName.toLowerCase();
            $("span.element")
                    .filter(function () {
                        return $(this).text() === tn;
                    })
                    .css("color", "red");

        });
        

    });

    //toggle the contents of practice
    $(".practice").click(function (e) {
        var posx = $(this).width() - e.pageX + $(this).offset().left;
        var posy = e.pageY - $(this).offset().top;
        console.log(posx);
        console.log(posy);
        console.log($(this).width());
        if (posx < 30 && posy < 50) {
            $(this).toggleClass("ahide");
        }
    });



});