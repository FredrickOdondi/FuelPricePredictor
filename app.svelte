<script>
  // Reactive variables to hold input and output values
  let crudeOilPrice = 0;
  let dieselPrice = 0;
  let petrolPrice = 0;
  let paraffinPrice = 0;

  // Function to calculate fuel prices based on crude oil price
  function calculatePrices() {
    // Example conversion rates (adjust as necessary)
    const dieselRatio = 0.12;
    const petrolRatio = 0.15;
    const paraffinRatio = 0.1;

    // Calculate the prices
    dieselPrice = (crudeOilPrice * dieselRatio).toFixed(2);
    petrolPrice = (crudeOilPrice * petrolRatio).toFixed(2);
    paraffinPrice = (crudeOilPrice * paraffinRatio).toFixed(2);
  }
</script>

<main>
  <h1>Crude Oil to Fuel Price Calculator</h1>

  <label for="crude">Enter Daily Crude Oil Price (USD):</label>
  <input
    id="crude"
    type="number"
    bind:value={crudeOilPrice}
    on:input={calculatePrices}
  />

  <h2>Calculated Prices (USD):</h2>
  <p><strong>Diesel:</strong> ${dieselPrice}</p>
  <p><strong>Petrol:</strong> ${petrolPrice}</p>
  <p><strong>Paraffin:</strong> ${paraffinPrice}</p>
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    margin: 20px;
    text-align: center;
  }

  label {
    font-weight: bold;
    display: block;
    margin-bottom: 10px;
  }

  input {
    margin-bottom: 20px;
    padding: 10px;
    font-size: 1rem;
  }

  h2 {
    margin-top: 20px;
  }

  p {
    font-size: 1.2rem;
  }
</style>
