<script>
  import { stateCtx, contactsForm } from '../../store.svelte';

  const fieldOrder = ['name', 'email', 'subject', 'message'];

  console.log(document.cookie.match(/csrftoken=([^;]+)/)?.[1]);

  async function handleSend() {
    const body = contactsForm();

    // В 2026 году Fetch — база. Не забудь про CSRF токен из кук!
    const response = await fetch('/', {
      method: 'POST',
      //   body: body,
      headers: {
        Accept: 'application/json',
        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)?.[1],
      },
    });

    const result = await response.json();
    if (result.status === 'success') {
      alert('Улетело!');
    }
  }
</script>

<div>
  <div class="contact-form">
    {#each fieldOrder as key}
      <!-- Берем конфиг поля из stateCtx.form (то, что прислал Django) -->
      {#if stateCtx.form[key]}
        {@const fieldConfig = stateCtx.form[key]}

        <div class="field-group">
          <label for={key}>{fieldConfig.label}</label>

          {#if key === 'subject'}
            <!-- Привязываем значение к contactsData -->
            <select id={key} bind:value={stateCtx.contactsData[key]}>
              <option value="">Выберите тему</option>
              {#each fieldConfig.choices as [val, label]}
                <option value={val}>{label}</option>
              {/each}
            </select>
          {:else if fieldConfig.input_type === 'textarea'}
            <textarea id={key} bind:value={stateCtx.contactsData[key]}></textarea>
          {:else}
            <input type={fieldConfig.input_type} id={key} bind:value={stateCtx.contactsData[key]} />
          {/if}
        </div>
      {/if}
    {/each}

    <button onclick={handleSend}> Отправить </button>
  </div>
</div>

<style>
  .field-group {
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
  }
  label {
    font-weight: bold;
    margin-bottom: 0.3rem;
  }
  textarea {
    min-height: 100px;
  }
</style>
