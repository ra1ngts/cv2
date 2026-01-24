<script>
  import { stateCtx, contactsForm } from '../../store.svelte';
  import { isEmailValidate, checkFields } from '../../utils';

  const ordering = ['name', 'email', 'subject', 'message'];

  async function handleSend() {
    stateCtx.formErrors = {};

    if (!stateCtx.contactsData.name) {
      stateCtx.formErrors['name'] = 'Enter your name';
    }

    if (!isEmailValidate(stateCtx.contactsData.email)) {
      stateCtx.formErrors['email'] = 'example@example.com';
    }

    if (!stateCtx.contactsData.subject) {
      stateCtx.formErrors['subject'] = 'Enter a subject';
    }

    if (!stateCtx.contactsData.message) {
      stateCtx.formErrors['message'] = 'Write a message';
    }

    if (Object.keys(stateCtx.formErrors).length > 0) {
      return;
    }

    const request = contactsForm();

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
        console.log('Message sent successfully');
      } else {
        const cleanedErrors = {};

        for (const [field, array] of Object.entries(result.errors)) {
          console.log('field, array', field, array);

          cleanedErrors[field] = array[0].message;
        }

        stateCtx.formErrors = cleanedErrors;
        console.log('stateCtx.formErrors', stateCtx.formErrors);

        console.log(result.message);
      }
    } catch (error) {
      console.error('Network Error:', error);
    }
  }

  $effect(() => {
    checkFields();
  });
</script>

<div class="space-y-4 max-w-md">
  {#each ordering as orderItem}
    {#if stateCtx.form[orderItem]}
      {@const field = stateCtx.form[orderItem]}

      <div class="flex flex-col">
        {#if field.input_type === 'textarea'}
          <textarea
            id={orderItem}
            name={orderItem}
            bind:value={stateCtx.contactsData[orderItem]}
            rows="5"
            placeholder={stateCtx.formErrors?.[orderItem] ? stateCtx.formErrors?.[orderItem] : field.label}
            class="block w-full rounded-2xl shadow-sm transition-all duration-300 outline-none p-2.5 border {stateCtx
              .formErrors?.[orderItem]
              ? 'border-red-500 focus:border-red-500 focus:ring-red-200/20'
              : 'border-gray-500 focus:border-cyan-200 focus:ring-cyan-200/10'}"
          ></textarea>
        {:else}
          <input
            type={field.input_type}
            id={orderItem}
            name={orderItem}
            bind:value={stateCtx.contactsData[orderItem]}
            placeholder={stateCtx.formErrors?.[orderItem] ? stateCtx.formErrors?.[orderItem] : field.label}
            required={field.required}
            class="block w-full rounded-2xl shadow-sm transition-all duration-300 outline-none p-2.5 border {stateCtx
              .formErrors?.[orderItem]
              ? 'border-red-500 focus:border-red-500 focus:ring-red-200/20'
              : 'border-gray-500 focus:border-cyan-200 focus:ring-cyan-200/10'}"
          />
        {/if}
      </div>
    {/if}
  {/each}

  <button
    onclick={handleSend}
    class="w-full py-3 px-4 bg-cyan-400 hover:bg-cyan-200 text-cyan-800 font-bold rounded-2xl transition-colors shadow-lg shadow-cyan-400/30"
  >
    Submit
  </button>
</div>
