//$(function(){ ... });

$(function(){
	for(var x = 1; x < 10; x++) {
		for(var y = 1; y < 10; y++) {
			var tag = $("<div>")
			tag.css({
				position: "absolute",
				top: x * 20 + "px",
				left: y * 20 + "px",
				width: "20px",
				height: "20px"
			})
			tag.attr({x: x, y: y})
			tag.text("*")
			tag.appendTo($("body"))
		}
	}

	$.getJSON("data.js", function(result){
		// var where = $("div[@x=\"" + result.x + "\"][@y=\"" + result.y + "\"]")
		// where.css("color", result.color)
		alert(result.x + "," + result.y)
	})
});

/*
for(var i = 1; i < 100; i++) {
	var new_div = $("<div>");
	if(i%2) { new_div.attr("class", "other"); }
	new_div.appendTo($("body"));
}

for(var n in $("div")){
	var x = n / 10;
	var y = n % 10;
	var elem = $("div")[n];
	var jqelem = $(elem);
	jqelem.css({
		position: "absolute",
		left: x * 20 + "px",
		top: y * 20 + "px",
		width: "20px",
		height: "20px",
		display: "block"
	});
}
*/
