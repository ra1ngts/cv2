<script>
  import { stateCtx } from '../../store.svelte';
</script>

<div>
  {#if stateCtx.projects.length > 0}
    {#each stateCtx.projects as item}
      <p>{item.title} — {item.description}</p>
    {/each}
  {/if}
</div>
