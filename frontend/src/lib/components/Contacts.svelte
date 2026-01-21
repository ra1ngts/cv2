<script>
  import { stateCtx, contactsForm } from '../../store.svelte';

  const ordering = ['name', 'email', 'subject', 'message'];

  async function handleSend() {
    const response = await fetch('/', {
      method: 'POST',
      body: contactsForm(stateCtx.contactsData),
      headers: {
        // Accept: 'application/json',
        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)?.[1],
      },
    });

    const result = await response.json();
    if (result.status === 'success') {
      console.log('Message sent successfully');
    }
  }
</script>

<div>
  {#each ordering as orderItem}
    {#if stateCtx.form[orderItem]}
      {@const field = stateCtx.form[orderItem]}

      <div>
        <label for={orderItem}>{field.label}</label>

        {#if orderItem === 'subject'}
          <select id={orderItem} bind:value={stateCtx.contactsData[orderItem]}>
            <option value="">Choose topic</option>
            {#each field.choices as [value, label]}
              <option {value}>{label}</option>
            {/each}
          </select>
        {:else if field.input_type === 'textarea'}
          <textarea id={orderItem} bind:value={stateCtx.contactsData[orderItem]}></textarea>
        {:else}
          <input type={field.input_type} id={orderItem} bind:value={stateCtx.contactsData[orderItem]} />
        {/if}
      </div>
    {/if}
  {/each}

  <button onclick={handleSend}>Submit</button>
</div>
