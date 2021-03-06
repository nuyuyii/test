
// -$("#scatter").load("{% url 'home' %}");-->



/* ******************************************************** */  
/* ***************** Onload Body HTML ********************* */
/* ******************************************************** */
var carsAndModels = {};
function makeBase(){
    carsAndModels['1'] = ['su', 'fd', 'id','tr','gsl','wsdi','csdi','dtr','txx','tnx','txn','tnn','tn10p','tx10p','tn90p','tx90p'];
    carsAndModels['2'] = ['rx1day', 'rx5day', 'sdii', 'r10mm','r20mm','rnnmm','cdd','cwd','r95ptot','r99ptot','prcptot'];
    ChangeCarList();
    //document.getElementById("tool").innerHTML = ind;
    ajaxData();   
}

/* ******************************************************** */  
/* ****************** Legend Color Map ******************** */
/* ******************************************************** */
// var nLegend = ["temperature (°C)", "preciptation (mm/day)"]
var nLegend = {"tem": {"color":["#4575b4", "#ffffbf", "#a50026"],
"name":"Temperature (°C)","domain":[-10, 20, 35],"scale":[-10, 40]},
"prec":{"color":["#ffffe5","#33FFCC","#00441b"],"name":"preciptation (mm/day)",
"domain":[-5, 2,14],"scale":[0, 15]}};
//["#543005","#FFFFFF","#2EFEF7","#003c30"]
//["#9F5000","#ffffe5","#0C6944"]
//"#543005","#7fcdbb","#2c7fb8"
//"prec":{"color":["#ffffe5","#33FFCC","#00441b"],"name":"preciptation (mm/day)",
//"domain":[-3, 5,18],"scale":[0, 20]}};
var indL = "tem";
var i_ticks = 15;  // max_value is scale/2

var legend = d3.select('#legend_p');

var widthL = parseInt(legend.style('width')),
    heightL = parseInt(legend.style('height'));

var color = d3.scale.linear()
    .domain(nLegend[indL]['domain'])
    .range(nLegend[indL]['color'])
    .interpolate(d3.interpolateHcl);

var x = d3.scale.linear()
    .domain(nLegend[indL]['scale'])
    .range([0, widthL-20]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .tickSize(20)
    .ticks(i_ticks)
    .tickFormat(d3.format("+.0f"));

//console.log("legend w/h",widthL,heightL);

var svgL = legend.append("svg")
    .attr("width", widthL)
    .attr("height", heightL)
    .attr("class", "legendP")
  .append("g")
    .attr("transform", "translate(10,30)");

svgL.selectAll("rect")
    .data(pair(x.ticks(i_ticks)))
  .enter().append("rect")
    .attr("height", 20)
    .attr("x", function(d) { return x(d[0]); })
    .attr("width", function(d) { return x(d[1]) - x(d[0]); })
    .style("fill", function(d) { return color(d[0]); });

svgL.call(xAxis).append("text")
    .attr("class", "caption")
    .attr("y", -10)
    .attr("x", widthL/2)
    .text(nLegend[indL]['name']);


function pair(array) {
  return array.slice(1).map(function(b, i) {
    //console.log(array[i], b);
    return [array[i], b];
  });
}

/* ******************************************************** */  
/* **************** Map Projection d3 plot **************** */
/* ******************************************************** */
var mapP = d3.select('#map_p');
//var tooltip = map.append("div").attr("class", "tooltip hidden");

var width = parseInt(mapP.style('width')),
height = parseInt(mapP.style('height'));

var graticule = d3.geo.graticule();
var zoomMap = d3.behavior.zoom().translate([0,0])//.center([117.9, 6.7])
                .scale(1).scaleExtent([1, 20]).on("zoom", moveMap);

function moveMap(){
    var t = d3.event.translate;
    var s = d3.event.scale;

    var w_max = 0;
    var w_min = width * (1 - s);
    var h_max = height < s*width/2 ? s*(width/2-height)/2 : (1-s)*height/2;
    var h_min = height < s*width/2 ? -s*(width/2-height)/2-(s-1)*height : (1-s)*height/2;

    t[0] = Math.min(w_max, Math.max(w_min, t[0]));
    t[1] = Math.min(h_max, Math.max(h_min, t[1]));

    console.log(t,s)

    zoomMap.translate(t);
    gMap.attr("transform", "translate(" + t + ")scale(" + s + ")");
    gMap.selectAll("path").attr("class","MapColor");
    //console.log(t,s);
    gMap2.attr("transform", "translate(" + t + ")scale(" + s + ")");
    gMap2.selectAll("path").style("stroke-width", .9 / s + "px");
}

// --------------------------------------
// --------------- setup map
var projection, pathMap, svgMap, gMap, gMap2;
setupMap(width,height);

console.log(width,height)

function setupMap(width,height){
               
    projection = d3.geo.equirectangular()
                .center([117.9, 6.7]).scale(width) //width/2/Math.PI
                .translate([width/2, height/2]);

    pathMap = d3.geo.path().projection(projection);
    svgMap = mapP
            .append("svg")
            .attr("width", '100%')
            .attr("height", '100%')
            .attr("class","svgMap")
            .call(zoomMap);

    gMap = svgMap.append("g"),
    gMap2 = svgMap.append("g");
}

// --------------------------------------
// --------------- port layer0 color map
var dataTs,dataLand,dataPr;

var data9T;
d3.json('../static/data/geoAvgTsPrG9.json', function(json) {
    console.log("FF",json.length);   
    data9T = json.features;
});

function drawMapL0(json){
    //data temp coordinate
// d.id 0-252 keep  d.coordinate[0][1] lon -180 to 180 
// d.id %252 keep d.coordinate[0][0] lat -90 to -90
    //console.log(json[1]);
    gMap.selectAll("path")
        .data(json)
        .enter().append("path")
        .attr("d", pathMap)
        .attr("class","MapColor")
        .style("fill", function(data9T){ return color(data9T.properties.allts);})
        .style("stroke",function(data9T){ return color(data9T.properties.allts);});
                    //.style("stroke-width",1)data9T
                    //.style("stroke-opacity",1);
                    //.style("opacity",1);
}

d3.json('../static/data/geoAvgTsPrG9t.json', function(json) {
    dataTs = json.features;
    var dou=[];
    //var tt = dataTs.properties.ts[1]
    console.log(data9T[0].properties.allts)
    dataTs.forEach(function(d, i){
    //dou.push(data9T[i].properties.allts)
        d.properties.allts = +data9T[i].properties.allts;
    })
                //console.log(dou)
    drawMapL0(dataTs);
});

            
           /*
            d3.json('../static/data/geoTsPrAvg.json', function(json) {
                console.log(json);
            });*/
// --------------------------------------
// --------------- Base map
d3.json('../static/data/world-topo-min.json', function(json) {
    dataLand = topojson.feature(json, json.objects.countries).features
    drawMapL1(dataLand);
});

function drawMapL1(json){
    gMap2.append("path")
          .datum(graticule)
          .attr("class","graticule")
          .attr("d", pathMap);

    gMap2.selectAll("path")
         .data(json)
         .enter().append("path")
         .attr("d", pathMap)
         .style("stroke-width",0.9);
                    //.attr("class","country");
                    //.style("fill","white");
                    /*.on("mousemove", function(d,i){
                        var mouse = d3.mouse(svgMap.node()).map( function(d) { return parseInt(d); } );
                        var left = Math.min(width-12*d.properties.name.length, (mouse[0]+20));
                        var top = Math.min(height-40, (mouse[1]+20));

                        tooltip.classed("hidden", false)
                            .attr("style", "left:"+left+"px;top:"+top+"px")
                            .html(d.properties.name);
                    })
                    .on("mouseout",  function(d,i) {
                        tooltip.classed("hidden", true);
                    });*/
}

// --------------------------------------
// --------------- Resize window
d3.select(window).on('resize', function() {
    width = parseInt(mapP.style('width'));
    height = parseInt(mapP.style('height'));

    projection.scale(width) //width/2/Math.PI
              .translate([width/2, height/2]);
    pathMap = d3.geo.path().projection(projection);
    gMap.selectAll("path")
        .attr("d", pathMap);

    gMap2.selectAll("path")
         .attr("d", pathMap);
});

// --------------------------------------
// --------------- Redraw Map
function resetMap(){
    width = parseInt(mapP.style('width'));
    height = parseInt(mapP.style('height'));
    console.log("Reset Ok");
    gMap.transition()
        .duration(500)
        .attr("transform","translater("+width/2+","+height/2+")scale(" +width+ ")");
        //.style("stroke-width", .5 + "px");
    gMap2.transition()
         .duration(500)
         .attr("transform","translater("+width/2+","+height/2+")scale(" +width+ ")")
         .style("stroke-width", .9 + "px");

               /* d3.select('.svgMap').remove();
                setupMap(width,height)
                drawMapL0(dataLand);
                drawMapL1(dataTs);
                setupMap(width,height);*/
};

d3.selectAll("button[resetP]").on("click", resetMap);

// --------------------------------------
// --------------- Zoom button
function zoomed() {
    svgMap.attr("transform",
        "translate(" + zoomMap.translate() + ")" +
        "scale(" + zoomMap.scale() + ")"
    );
}

function interpolateZoom (t, s) {
    var self = this;
    d3.transition().duration(350).tween("zoom", function () {      

        var iTranslate = d3.interpolate(zoomMap.translate(), t),
            iScale = d3.interpolate(zoomMap.scale(), s);
            console.log("call interpolateZoom");
        return function (tr) {
            zoomMap
                .scale(iScale(tr))
                .translate(iTranslate(tr));
            zoomed();
        };
    });
}

function zoomClick() {
    var clicked = d3.event.target,
        direction = 1,
        factor = 0.2,
        target_zoom = 1,
        center = [width / 2, height / 2],
        extent = zoomMap.scaleExtent(),
        translate = zoomMap.translate(),
        translate0 = [],
        l = [],
        view = {x: translate[0], y: translate[1], k: zoomMap.scale()};
    console.log(translate,extent);
    d3.event.preventDefault();
    direction = (this.id === 'zoom_in') ? 1 : -1;
    target_zoom = zoomMap.scale() * (1 + factor * direction);

    if (target_zoom < extent[0] || target_zoom > extent[1]) { return false; }

    translate0 = [(center[0] - view.x) / view.k, (center[1] - view.y) / view.k];
    view.k = target_zoom;
    l = [translate0[0] * view.k + view.x, translate0[1] * view.k + view.y];

    view.x += center[0] - l[0];
    view.y += center[1] - l[1];

    console.log(l,translate0,view);
    //interpolateZoom([view.x, view.y], view.k);
}

//d3.selectAll('button[zoomP]').on('click', zoomClick);


