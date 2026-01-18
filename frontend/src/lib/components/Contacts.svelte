<script>
  import { stateCtx } from '../../store.svelte';
</script>

<div>
  {#each Object.entries(stateCtx.form) as [k, v]}
    {k} {v}
  {/each}
</div>
