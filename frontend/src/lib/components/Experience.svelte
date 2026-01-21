<script>
  import { stateCtx } from '../../store.svelte';
  import { getDuration } from '../../utils';
</script>

{#if stateCtx.experience.length > 0}
  {#each stateCtx.experience as entry}
    <a href={entry.company_url} target="_blank" rel="noopener noreferrer" class="group block">
      <div
        class="grid grid-cols-2 gap-4 p-4 rounded-2xl transition-all duration-300 hover:bg-white/5 hover:backdrop-blur-md
        hover:shadow-2xl hover:shadow-cyan-950/20"
      >
        <div class="text-gray-400">
          {getDuration(entry.start_date, entry.end_date, entry.is_current)}
        </div>

        <div class="grid grid-cols-1 gap-4">
          <div class="text-gray-300 font-semibold text-lg transition-colors duration-300 group-hover:text-cyan-200">
            {entry.position}, {entry.company}
          </div>

          <div class="text-sm">
            {entry.achievements}
          </div>

          {#if entry.skills && entry.skills.length > 0}
            <div class="flex flex-wrap flex-row gap-4">
              {#each entry.skills as skill}
                {#if skill.category.name !== 'Certificate'}
                  <div
                    class="flex gap-2 items-center rounded-2xl px-4 py-1 transition-colors duration-300 group-hover:text-cyan-200 bg-gray-900 group-hover:bg-gray-800"
                  >
                    {#if skill.image}
                      <img src={skill.image} alt={skill.name} class="w-6 h-6 object-contain" />
                    {/if}

                    <div class="text-sm font-semibold">
                      {skill.name}
                    </div>
                  </div>
                {/if}
              {/each}
            </div>
          {/if}
        </div>
      </div>
    </a>
  {/each}
{:else}
  <p>No entries available</p>
{/if}
