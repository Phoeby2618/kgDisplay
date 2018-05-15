function s(edges){

    var nodes = {};

    edges.forEach(function(link) {
      link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
      link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
    });

        console.log(nodes)
        console.log(edges)

		//initial data
		var width=600,height=500;

		var svg=d3.select("#display")
					.append("svg")
					.attr("id","c")
					.attr("width",width)
					.attr("height",height)
					
		//define force layout
		var force=d3.layout.force()
					.nodes(d3.values(nodes))
					.links(edges)
					.size([width,height])
					.linkDistance(180)
					.charge([-1000]);
			force.start();
			

		
		 //var color = d3.scale.category20();
		 
		//append line,nodes,text     先添加结点，再添加连线，即可将圆上的连线盖住
		
		var svg_lines=svg.selectAll("line")
						.data(edges)
						.enter()
						.append("line")
						.attr("stroke","#ccc")
						.attr("stroke-width",1);
						
		var svg_nodes=svg.selectAll("circle")
						.data(force.nodes())
						.enter()
						.append("circle")
						.style("fill",function(d,i){
							var color="#FFFFCC";
							if(i>=1&&i<edges.length+1){
								if( edges[i-1].rela=="checking"){
									color="#999933";
								}else if(edges[i-1].rela=="disease"){
								    color="#cc9999";
								}else if(edges[i-1].rela=="symptom")
									color="#9999cc";
							}
							return color;
						})
						.attr("r",20)
						.call(force.drag)       //节点可拖动;
						.on("click",function(d,i){                      //节电可点击
						    if(i!=0){
						        $("#inputkuang").val("");

                                console.log(i);
                                console.log(d.name);
                                console.log(d);
                                var type;
                                for(var j=0;j<edges.length;j++){

                                    if(edges[j].target.name==d.name){
                                        type=edges[j].rela;
                                        break;
                                        }
                                }
                                console.log(type);

                                $("#c").remove();
                                $("br").remove();
                                 $("span").remove();


                                if(d != null){
                                    $.get("/knowledge/look/",{'text':d.name,'type':type},function(dataResponse){
                                        if(dataResponse=="no items!")
                                            alert("查不到呀！");
                                        else{
                                            console.log(dataResponse[0][name]);
                                            for(var key in dataResponse[0]){
                                                console.log(key);
                                                //知识卡片更新
                                                d3.select("#attrs")
                                                    .append("span")
                                                    .text(key+":"+dataResponse[0][key])
                                                    .append("br");
                                                d3.select("#attrs").append("br");


                                            }
                                            console.log(dataResponse[1])
                                            var edges=dataResponse.slice(1,dataResponse.length);

                                            s(edges);
                                        }
                                    });
                                 }
                            }
						});
						
		
		
		var svg_texts=svg.selectAll("text")
						.data(force.nodes())
						.enter()
						.append("text")
						.style("fill", "black")
						.attr("dx", 18)
						.attr("dy", 8)
						.text(function(d){
							return d.name;
						});
		
		<!--var svg_line_text=svg.selectAll(".linetext")-->
						<!--.data(edges)-->
						<!--.enter()-->
						<!--.append("text")-->
						<!--.text(function(d){-->
							<!--return d.rela;-->
						<!--});			-->

		force.on("tick",function(){
				svg_nodes.attr("cx",function(d){
						return d.x;
						})
						.attr("cy",function(d){
						return d.y;
						});
				svg_lines.attr("x1",function(d){
							return d.source.x;
						})
						.attr("y1",function(d){
							return d.source.y;
						})
						.attr("x2",function(d){
							return d.target.x;
						})
						.attr("y2",function(d){
							return d.target.y;
						});
				svg_texts.attr("x",function(d){
							return d.x;
						})
						.attr("y",function(d){
							return d.y;
						});
				<!--svg_line_text.attr("x",function(d){-->
							<!--return (d.source.x+d.target.x)/2;-->
						<!--})-->
						<!--.attr("y",function(d){-->
							<!--return (d.source.y+d.target.y)/2;-->
						<!--})				-->
		});
}