<script>
  import { stateCtx, contactsForm } from '../../store.svelte';

  const ordering = ['name', 'email', 'subject', 'message'];

  async function handleSend() {
    const response = await fetch('/', {
      method: 'POST',
      body: contactsForm(),
      headers: {
        Accept: 'application/json',
        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)?.[1],
      },
    });

    const result = await response.json();
    if (result.status === 'success') {
      console.log('Message sent successfully');
    }
  }
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
            placeholder={field.label}
            class="block w-full rounded-2xl border-gray-500 shadow-sm focus:border-cyan-200 focus:ring-4 focus:ring-cyan-200/10 transition-colors duration-300 outline-none p-2.5 border"
          ></textarea>
        {:else}
          <input
            type={field.input_type}
            id={orderItem}
            name={orderItem}
            bind:value={stateCtx.contactsData[orderItem]}
            placeholder={field.label}
            required={field.required}
            class="block w-full rounded-2xl border-gray-500 shadow-sm focus:border-cyan-200 focus:ring-4 focus:ring-cyan-200/10 transition-colors duration-300 outline-none p-2.5 border"
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
