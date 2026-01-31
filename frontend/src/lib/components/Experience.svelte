<script>
  import { stateCtx } from '../../store.svelte';
  import { getDuration } from '../../utils';
</script>

{#if stateCtx.experience.length > 0}
  {#each stateCtx.experience as entry}
    <a href={entry.company_url} target="_blank" rel="noopener noreferrer" class="group block">
      <div
        class="grid sm:grid-cols-3 grid-cols-1 sm:gap-4 gap-2 p-2 md:p-4 rounded-2xl transition-all duration-300 hover:bg-white/5 hover:backdrop-blur-md
        hover:shadow-2xl hover:shadow-cyan-950/20"
      >
        <div class="col-span-1">
          <div class="text-gray-400">
            {getDuration(entry.start_date, entry.end_date, entry.is_current)}
          </div>
        </div>

        <div class="col-span-2">
          <div class="grid grid-cols-1 sm:gap-4 gap-2">
            <h3
              class="text-gray-300 font-semibold text-sm sm:text-lg md:text-2xl transition-colors duration-300 group-hover:text-cyan-200"
            >
              {entry.position}, {entry.company}
            </h3>

            <div class="text-sm">
              {entry.achievements}
            </div>

            {#if entry.skills && entry.skills.length > 0}
              <div class="flex flex-wrap flex-row gap-2">
                {#each entry.skills as skill}
                  {#if skill.category.name !== 'Certificate'}
                    <div class="flex items-center">
                      {#if skill.image}
                        <img src={skill.image} alt={skill.name} class="flex w-full h-6 object-cover" />
                      {/if}
                    </div>
                  {/if}
                {/each}
              </div>
            {/if}
          </div>
        </div>
      </div>
    </a>
  {/each}
{:else}
  <p>No entries available</p>
{/if}
