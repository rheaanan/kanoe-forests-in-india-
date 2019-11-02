var report = "A Multiple Linear Regression was calculated to predict Forest-cover in India based on Rainfall, Population Density and Temperature.\r\nA significant regression equation was found F (3 , 1117) = (168.588 , p<0.000) with an R2 of 0.312. From the adjusted R2 we can report that about 31.2% of variability in forest-cover is explained by the model.\nThe p-value or significance is below .05 and hence we can’t reject the model.\
Now we can say from the unstandardized coefficients that increase in rainfall by 1mm across the country will cause 0.011% increase in forest-cover of India with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet then forest-cover can decrease by 0.001%. If there is an increase in temperature by 1 degree Celsius due to global warming and other factors then there is a possibility of 2.43% decrease of forest-cover.";
document.getElementById("predtext").textContent = report;
function change()
{
	var x = document.getElementById("predselect");
	var img = document.getElementById("timg");
	if(x.value == "deccanplateau")
	{
		img.src = "img/deccanplateau.png"
		report = "A Multiple Linear Regression calculated to predict Forest-cover in Deccan Plateau Region of India. A significant regression equation was found F (3, 346) = (38.094, p<0.000) with an R2 of 0.248. From the adjusted R2 we can report that about 25% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now we can say from the unstandardized coefficients that increase in rainfall by 1mm across the country will cause 0.018% increase in forest-cover of Deccan Plateau region with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet then forest-cover can decrease by 0.017%. But even if there is an increase in temperature by 1 degree Celsius, there is a possibility of .839% increase of forest-cover. This prediction is made mostly because over the years even when there was increase in temperature there is no much difference in the forest-cover  in states like Madhya Pradesh and Maharashtra.";
	}
	
	else if(x.value == "coastal")
	{
		img.src = "img/coastal.png"
		report="A Multiple Linear Regression calculated to predict Forest-cover in Coastal Areas of India. A significant regression equation was found F (3,140) = (122.476, p<0.000) with an R2 of 0.724. From the adjusted R2 we can report that about 72.4% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.012% increase in forest-cover with the population density and temperature remaining constant. But even if there is increase in population density by 1 unit i.e. one more person per square feet also there is no much change in forest-cover. If there is an increase in temperature by 1 degree Celsius, there is a possibility of 2.67% increase of forest-cover.";
	}
	
	else if(x.value == "central")
	{
		img.src = "img/centralhighlands.png"
		report="A Multiple Linear Regression calculated to predict Forest-cover in Central Highlands of India. A significant regression equation was found F (3,166) = (18.29, p<0.000) with an R2 of 0.248. From the adjusted R2 we can report that about 25% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.01% increase in forest-cover with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet also there is 0.017% decrease in forest-cover. If there is an increase in temperature by 1 degree Celsius, there is a possibility of 2.119% increase in forest-cover.";
	}
	
	else if(x.value == "nplains")
	{
		img.src = "img/northernplains.png"
		report="A Multiple Linear Regression calculated to predict Forest-cover in Northern Plains of India. A significant regression equation was found F (3,129) = (6.156, p<0.001) with an R2 of 0.125. From the adjusted R2 we can report that about 12.5% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.007% increase in forest-cover with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet also there is 0.003% decrease in forest-cover. However if there is an increase in temperature by 1 degree Celsius, there is a possibility of 1.046% increase in forest-cover.";
		
	}
	
	else if(x.value == "eplains")
	{
		img.src = "img/easternplains.png"
		report="A Multiple Linear Regression calculated to predict Forest-cover in Eastern Plains of India. A significant regression equation was found F (3, 65) = (103.366, p<0.000) with an R2 of 0.827. From the adjusted R2 we can report that about 82.7% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.003% increase in forest-cover with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet also there is 0.003% decrease in forest-cover. If there is an increase in temperature by 1 degree Celsius, there will be a significant decrease of 10.996% for forest-cover.";
	}
	
	else if(x.value == "wplains")
	{
		img.src = "img/westernplains.png"
		report = "A Multiple Linear Regression calculated to predict Forest-cover in Western Plains of India. A significant regression equation was found F (3, 34) = (18.794, p<0.000) with an R2 of 0.624. From the adjusted R2 we can report that about 62.4% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.005% increase in forest-cover with the population density and temperature remaining constant. It is found that if there is increase in population density by 1 unit i.e. one more person per square feet there is 0.014% decrease in forest-cover. And if there is an increase in temperature by 1 degree Celsius, there will be an increase of 0.444% for forest-cover.";
	}
	else if(x.value == "mountains")
	{
		img.src = "img/northernmountains.png"
		
		report="A Multiple Linear Regression calculated to predict Forest-cover in in Northern Mountains of India. A significant regression equation was found F (3, 199) = (24.094, p<0.000) with an R2 of 0.266. From the adjusted R2 we can report that about 26.6% of variability in forest-cover is explained by the model. The p-value is below .05 and hence we can’t reject the model. Now the increase in rainfall by 1mm across the country will cause 0.005% increase in forest-cover with the population density and temperature remaining constant. It is found that if there is increase in population density by 1 unit i.e. one more person per square feet there is 0.049% decrease in forest-cover. But if there is an increase in temperature by 1 degree Celsius, there will be an increase of 0.610% for forest-cover.";
	}
	else if(x.value == "india")
	{
		img.src = "img/India.png"
		report = "A Multiple Linear Regression was calculated to predict Forest-cover in India based on Rainfall, Population Density and Temperature.\r\nA significant regression equation was found F (3 , 1117) = (168.588 , p<0.000) with an R2 of 0.312. From the adjusted R2 we can report that about 31.2% of variability in forest-cover is explained by the model.\nThe p-value or significance is below .05 and hence we can’t reject the model.\
Now we can say from the unstandardized coefficients that increase in rainfall by 1mm across the country will cause 0.011% increase in forest-cover of India with the population density and temperature remaining constant. Similarly if there is increase in population density by 1 unit i.e. one more person per square feet then forest-cover can decrease by 0.001%. If there is an increase in temperature by 1 degree Celsius due to global warming and other factors then there is a possibility of 2.43% decrease of forest-cover.";
	}
	
	
	document.getElementById("predtext").textContent = report;
}