	var carsAndModels = {};
    carsAndModels['1'] = ['su', 'fd', 'id','tr','gsl','wsdi','csdi','dtr','txx','tnx','txn','tnn','tn10p','tx10p','tn90p','tx90p'];
    carsAndModels['2'] = ['rx1day', 'rx5day', 'sdii', 'r10mm','r20mm','rnnmm','cdd','cwd','r95ptot','r99ptot','prcptot'];

    function ChangeCarList() {
        var carList = document.getElementById("vars");
        var modelList = document.getElementById("cindex");
        var selCar = carList.options[carList.selectedIndex].value;

        console.log(selCar);

        while (modelList.options.length) {
            modelList.remove(0);
        }
        var cars = carsAndModels[selCar];
        if (cars) {
            var i;
            for (i = 0; i < cars.length; i++) {
                var car = new Option(cars[i], i);
                modelList.options.add(car);
            }
        }
    } 

