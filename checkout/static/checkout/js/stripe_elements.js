// Retrieve the public key and client secret from the DOM
var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim().slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.trim().slice(1, -1);

// Initialize Stripe and its elements
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Define the style for the card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create and mount the card element
var card = elements.create('card', { style: style });
card.mount('#card-element');
