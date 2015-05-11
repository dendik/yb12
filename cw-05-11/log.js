x = {a:1, "b":2, 34:5}
x.a
x["a"]
x.b
class_B = function(){ this.a = 1; }
class_B.prototype = x
a = new class_B()
b = new class_B()
String(a)
x.a = 42
a.b
a.a
x.z = 666
a.z
a.z = 33
a.z
x.z
$
jQuery
for(var i = 1; i < 100; i++) { var new_div = $("<div>");
for(var i = 1; i < 100; i++) { var new_div = $("<div>"); if(i%2) { new_div.attr("class", "other"); } new_div.appendTo($("body")); }
$("div").text("*")
var all_divs_in_page = $("div")
var new_div_tag = $("<div>")
$("div.other").css("color", "red")
$("div").css("display", "inline")
for(var n in $("div")){ var x = n / 10; var y = n % 10; var elem = $("div")[n]; elem.css("color", "blue"); }
for(var n in $("div")){ var x = n / 10; var y = n % 10; var elem = $("div")[n]; var jqelem = $(elem); elem.css("color", "blue"); }
for(var n in $("div")){ var x = n / 10; var y = n % 10; var elem = $("div")[n]; var jqelem = $(elem); jqelem.css("color", "blue"); }
for(var n in $("div")){ var x = n / 10; var y = n % 10; var elem = $("div")[n]; var jqelem = $(elem); jqelem.css({position: "absolute", left: x * 20 + "px", top: y * 20 + "px", width: "20px", height: "20px", display: "block" }); }
