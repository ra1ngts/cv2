<script>
  import { stateCtx } from '../../store.svelte';
  import { getDuration } from '../../utils';
</script>

{#each stateCtx.experience as field}
  <a href={field.company_url} target="_blank" rel="noopener noreferrer" class="group block">
    <div
      class="grid grid-cols-2 gap-4 p-4 rounded-2xl transition-all duration-300 hover:bg-white/5 hover:backdrop-blur-md
        hover:shadow-2xl hover:shadow-cyan-950/20"
    >
      <div class="text-gray-400">
        {getDuration(field.start_date, field.end_date, field.is_current)}
      </div>

      <div class="grid grid-cols-1 gap-4">
        <div class="text-gray-300 font-semibold text-lg transition-colors duration-300 group-hover:text-cyan-200">
          {field.position}, {field.company}
        </div>

        <div class="text-sm">
          {field.achievements}
        </div>
      </div>
    </div>
  </a>
{/each}
