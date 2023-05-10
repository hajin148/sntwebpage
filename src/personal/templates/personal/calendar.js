var app = angular.module('calendarApp', []);

app.controller('calendarController', ['$scope', function($scope) {
    const today = new Date();
    $scope.year = today.getFullYear();
    $scope.month = today.getMonth();
    $scope.today = today;

    $scope.prev = function() {
        $scope.month--;
        if ($scope.month < 0) {
            $scope.month = 11;
            $scope.year--;
        }
        $scope.generateDays();
    };

    $scope.next = function() {
        $scope.month++;
        if ($scope.month > 11) {
            $scope.month = 0;
            $scope.year++;
        }
        $scope.generateDays();
    };

    $scope.generateDays = function() {
        const monthStart = new Date($scope.year, $scope.month, 1);
        const monthEnd = new Date($scope.year, $scope.month + 1, 0);
        $scope.daysInMonth = monthEnd.getDate();
        $scope.startDay = monthStart.getDay();

        const daysArray = [];
        for (let i = 1; i <= $scope.daysInMonth; i++) {
            daysArray.push(i);
        }

        $scope.dates = daysArray;
    };

    $scope.getMonthName = function(month) {
        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        return monthNames[month];
    };

    $scope.generateDays();
}]);
