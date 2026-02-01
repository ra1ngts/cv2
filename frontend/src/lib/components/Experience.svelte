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
        <div class="col-span-1 flex items-center gap-2 [&_svg]:fill-gray-400">
          <div>
            <svg class="w-full h-6 object-cover" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"
              ><path
                d="M120 0c13.3 0 24 10.7 24 24l0 40 160 0 0-40c0-13.3 10.7-24 24-24s24 10.7 24 24l0 40 32 0c35.3 0 64 28.7 64 64l0 288c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 128C0 92.7 28.7 64 64 64l32 0 0-40c0-13.3 10.7-24 24-24zm0 112l-56 0c-8.8 0-16 7.2-16 16l0 48 352 0 0-48c0-8.8-7.2-16-16-16l-264 0zM48 224l0 192c0 8.8 7.2 16 16 16l320 0c8.8 0 16-7.2 16-16l0-192-352 0z"
              /></svg
            >
          </div>

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
                    <div class="flex items-center rounded-full bg-gray-800 p-2 sm:p-3">
                      {#if skill.image}
                        <img src={skill.image} alt={skill.name} class="flex w-4 h-4 sm:w-6 sm:h-6 object-contain" />
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
