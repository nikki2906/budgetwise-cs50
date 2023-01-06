//Calculate Tip
function calculateBudget() {
    var amount = Number(document.getElementById("amount").value);
    console.log(typeof amount)

    var budgetAmount = Number(document.getElementById("budgetPercent").value);

    //validate input
    if (amount === "" || budgetAmount == 0) {
      alert("Please enter values");
      return;
    }

    //Calculate appropriate budget amount
    var total = amount * budgetAmount;

    //Round to two decimal places
    total = Math.round(total * 100) / 100;
    total = total.toFixed(2);

    //Display the budget amount
    document.getElementById("totalBudget").style.display = "block";
    document.getElementById("budget").innerHTML = total;
  }

  //Hide the tip amount on load
  document.getElementById("totalBudget").style.display = "none";

  //click to call function
  document.getElementById("calculate").onclick = function() {
    calculateBudget();

  };

//Cited work: https://stackoverflow.com/questions/70110454/tip-calculator-javascript and https://codepen.io/cphemm/pen/reNwWd