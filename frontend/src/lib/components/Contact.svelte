<script>
  import { stateCtx, contactForm } from '../../store.svelte';
  import { isEmailValidate, markAsTouched, checkFields, showToast } from '../../utils';

  const ordering = ['name', 'email', 'subject', 'message'];

  markAsTouched();

  async function handleSend() {
    stateCtx.formErrors = {};
    if (stateCtx.isSubmitting) return;

    stateCtx.isSubmitting = true;

    ordering.forEach((key) => (stateCtx.touchedFields[key] = true));

    checkFields();

    if (!stateCtx.contactsData.name) {
      stateCtx.formErrors['name'] = 'Please enter your name';
    }

    if (!isEmailValidate(stateCtx.contactsData.email)) {
      stateCtx.formErrors['email'] = 'Enter a valid email address';
    }

    if (!stateCtx.contactsData.subject) {
      stateCtx.formErrors['subject'] = 'Please enter a subject';
    }

    if (!stateCtx.contactsData.message) {
      stateCtx.formErrors['message'] = 'Message is required';
    }

    if (Object.keys(stateCtx.formErrors).length > 0) {
      stateCtx.isSubmitting = false;
      return;
    }

    let retry = 0;

    while (typeof window.grecaptcha === 'undefined' || !window.grecaptcha.execute) {
      await new Promise((r) => setTimeout(r, 100));
      if (retry++ > 50) throw new Error('reCAPTCHA load timeout');
    }

    const token = await new Promise((resolve, reject) => {
      window.grecaptcha.ready(() => {
        window.grecaptcha.execute(window.RECAPTCHA_SITE_KEY, { action: 'submit' }).then(resolve).catch(reject);
      });
    });

    if (!token) throw new Error('Failed to generate captcha token');

    const request = contactForm(token);

    try {
      const response = await fetch('/', {
        method: 'POST',
        body: request,
        headers: {
          Accept: 'application/json',
          'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)?.[1],
          'X-Requested-With': 'XMLHttpRequest',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();

      if (result.status === 'success') {
        stateCtx.contactsData = { name: '', email: '', subject: '', message: '' };
        showToast('Message sent successfully!', 'success');
        console.log('Message sent successfully!');
      } else {
        const cleanedErrors = {};

        for (const [field, array] of Object.entries(result.errors)) {
          console.log('field, array', field, array);

          cleanedErrors[field] = array[0]?.message;
        }

        stateCtx.formErrors = cleanedErrors;
        console.log('stateCtx.formErrors', stateCtx.formErrors);

        console.log(result.message);
      }
    } catch (error) {
      console.error('Network Error:', error);
    } finally {
      stateCtx.isSubmitting = false;
    }
  }
</script>

<div class="space-y-4 max-w-md">
  {#each ordering as orderItem}
    {#if stateCtx.form[orderItem]}
      {@const field = stateCtx.form[orderItem]}
      {@const showError = stateCtx.touchedFields[orderItem] && stateCtx.formErrors[orderItem]}

      <div class="flex flex-col">
        {#if field.input_type === 'textarea'}
          <textarea
            id={orderItem}
            name={orderItem}
            bind:value={stateCtx.contactsData[orderItem]}
            onblur={() => markAsTouched(orderItem)}
            oninput={() => stateCtx.touchedFields[orderItem] && checkFields()}
            rows="5"
            placeholder={showError ? stateCtx.formErrors[orderItem] : field.label}
            class="block w-full rounded-2xl shadow-sm transition-all duration-300 outline-none p-2.5 border {showError
              ? 'border-red-500 focus:border-red-500 focus:ring-red-200/20'
              : 'border-gray-500 focus:border-cyan-200 focus:ring-cyan-200/10'}"
          ></textarea>
        {:else}
          <input
            type={field.input_type}
            id={orderItem}
            name={orderItem}
            bind:value={stateCtx.contactsData[orderItem]}
            onblur={() => markAsTouched(orderItem)}
            oninput={() => stateCtx.touchedFields[orderItem] && checkFields()}
            placeholder={showError ? stateCtx.formErrors[orderItem] : field.label}
            required={field.required}
            class="block w-full rounded-2xl shadow-sm transition-all duration-300 outline-none p-2.5 border {showError
              ? 'border-red-500 focus:border-red-500 focus:ring-red-200/20'
              : 'border-gray-500 focus:border-cyan-200 focus:ring-cyan-200/10'}"
          />
        {/if}
      </div>
    {/if}
  {/each}

  <button
    onclick={handleSend}
    disabled={stateCtx.isSubmitting}
    class="disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-cyan-400 disabled:shadow-none w-full py-3 px-4 bg-cyan-400 hover:bg-cyan-200 text-cyan-800 font-bold rounded-2xl transition-colors duration-300 shadow-lg shadow-cyan-400/30"
  >
    {stateCtx.isSubmitting ? 'Sending...' : 'Submit'}
  </button>
</div>
