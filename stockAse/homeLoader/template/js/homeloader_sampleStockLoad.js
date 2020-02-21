var genLine = () => $.ajax({
    type: "get",
    url: 'sample/test_data',
    success: (response) => {
        // console.log(response)
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: response.x_axis,
                datasets: [{
                    label: 'opening -> ',
                    data: response.y_axis ,
                    backgroundColor: 'rgba(0,0,0,0)',
                    borderColor: 'rgba(0,125,255,1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
})

var genLine2 = () => $.ajax({
    type: "get",
    url: 'sample/test_data',
    success: (response) => {
        // console.log(response)
        var ctx = document.getElementById('myChart2').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: response.x_axis,
                datasets: [{
                    label: 'opening -> ',
                    data: response.y_axis ,
                    backgroundColor: 'rgba(0,0,0,0)',
                    borderColor: 'rgba(0,125,255,1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
})


// initial load values
genLine()
genLine2()