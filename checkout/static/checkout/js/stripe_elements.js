/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
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
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    document.getElementById('submit-button').setAttribute('disabled', true);

    const toggleVisibility = (id) => {
        const element = document.getElementById(id);
        element.style.display = element.style.display === 'none' || !element.style.display ? 'block' : 'none';
    };

    toggleVisibility('payment-form');
    toggleVisibility('loading-overlay');

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                email: form.email.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    state: form.county.value.trim()
                }
            }
        },
        shipping: {
            name: form.full_name.value.trim(),
            phone: form.phone_number.value.trim(),
            address: {
                line1: form.street_address1.value.trim(),
                line2: form.street_address2.value.trim(),
                city: form.town_or_city.value.trim(),
                country: form.country.value.trim(),
                postal_code: form.postcode.value.trim(),
                state: form.county.value.trim()
            }
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            errorDiv.innerHTML = html;

            toggleVisibility('payment-form');
            toggleVisibility('loading-overlay');
            
            card.update({ 'disabled': false });
            document.getElementById('submit-button').removeAttribute('disabled');
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
