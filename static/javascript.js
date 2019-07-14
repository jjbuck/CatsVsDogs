var app = angular.module('mysfitsApp', []);
var mysfitsApiEndpoint = 'http://mysfits-nlb-cb6ebf9451d97ad8.elb.us-west-2.amazonaws.com';
var gridScope;
var data;
/*
    Reload the grid of mysfits whenever a new list is retrieved based
    on the filters selected.
*/
function applyGridScope(mysfitsList) {
    gridScope.mysfits = mysfitsList;
    gridScope.$apply();
}

/*
      Populate the main mysfit grid on page load.
    */
app.controller('mysfitsListController', function ($scope) {
    gridScope = $scope;
    getAllMysfits(applyGridScope);
});

function testApply(foo) {
    console.log(foo);
    data.responses = foo
    console.log(data.responses);
    data.$apply()
}

app.controller('testController', function ($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://FooTe-Netwo-6NQP0MX5N0L9-b79fa7b19992ea5b.elb.us-west-2.amazonaws.com',
    }).then(function (response) {
        console.log(response.data)
        $scope.response = response.data;
        console.log($scope.response)
        //alert($scope.response);
    });
});

/*
    Retrieve the full list of mysfits from the backend service API.
*/
function getAllMysfits(callback) {
    var mysfitsApi = mysfitsApiEndpoint + '/mysfits';
    $.ajax({
        url: mysfitsApi,
        type: 'GET',
        success: function (response) {
            callback(response.mysfits);
        },
        error: function (response) {
            console.log("could not retrieve mysfits list.");
            console.log(response.message);
        }
    });
}


function getTest(callback) {
    var mysfitsApi = 'https://jsonplaceholder.typicode.com/posts';
    $.ajax({
        url: mysfitsApi,
        type: 'GET',
        success: function (response) {
            console.log(response);
            callback(response);
        },
        error: function (response) {
            console.log("could not retrieve mysfits list.");
            console.log(response.message);
        }
    });
}






$(document).ready(function () {
    var $status = $('.status');

    $('#img').change(function (event) {
        var obj = $(this)[0];

        $status.html('');

        if (obj.files && obj.files[0]) {
            var fileReader = new FileReader();
            fileReader.onload = function (event) {
                $('.img-area').html(
                    `<img class='loaded-img' src='${event.target.result}' style="width:500px;height:500px;"/>`
                );
            }
            fileReader.readAsDataURL(obj.files[0]);
        }
    });

    $('form').submit(function (event) {
        event.preventDefault();

        if ($('#img')[0].files.length === 0) {
            return false;
        }

        var imageData = new FormData($(this)[0]);

        $status.html(
            `<span class='eval'>Evaluating...</span>`
        );

        $.ajax({
            url: '/is-hot-dog',
            type: 'POST',
            processData: false,
            contentType: false,
            dataType: 'json',
            data: imageData,

            success: function (responseData) {
                if (responseData.is_hot_dog === 'true') {
                    $status.html(
                        `<span class='result success'>Hot Dog</span>
                         <span class='confidence'>${responseData.confidence}% confident</span>`
                    );
                } else {
                    if (responseData.error === 'bad-type') {
                        $status.html(
                            `<span class='eval'>Valid file types are .jpg and .png</span>`
                        );
                    } else {
                        $status.html(
                            `<span class='result failure'>Not Hot Dog</span>`
                        );
                    }
                }
            },
            error: function () {
                $status.html(
                    `<span class='eval'>Something went wrong, try again later.</span>`
                );
            }
        });
    });

});



