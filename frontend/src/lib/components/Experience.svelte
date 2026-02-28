<script>
  import { stateCtx } from '../../store.svelte';
  import { getDuration } from '../../utils';
</script>

{#if stateCtx.experience.length > 0}
  {#each stateCtx.experience as entry}
    <a href={entry.company_url} target="_blank" rel="noopener noreferrer" class="group block">
      <div
        class="grid sm:grid-cols-3 mb-4 grid-cols-1 sm:gap-4 gap-2 p-2 md:p-4 rounded-2xl transition-all duration-300 bg-white/5 shadow-2xl backdrop-blur-md hover:bg-white/5 lg:bg-transparent lg:hover:backdrop-blur-md
        lg:hover:shadow-2xl lg:hover:shadow-cyan-950/20"
      >
        <div class="col-span-1 flex gap-2 [&_svg]:fill-gray-500">
          <div>
            <svg class="w-full h-6 object-cover" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"
              ><path
                d="M120 0c13.3 0 24 10.7 24 24l0 40 160 0 0-40c0-13.3 10.7-24 24-24s24 10.7 24 24l0 40 32 0c35.3 0 64 28.7 64 64l0 288c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 128C0 92.7 28.7 64 64 64l32 0 0-40c0-13.3 10.7-24 24-24zm0 112l-56 0c-8.8 0-16 7.2-16 16l0 48 352 0 0-48c0-8.8-7.2-16-16-16l-264 0zM48 224l0 192c0 8.8 7.2 16 16 16l320 0c8.8 0 16-7.2 16-16l0-192-352 0z"
              /></svg
            >
          </div>

          <div>
            {getDuration(entry.start_date, entry.end_date, entry.is_current)}
          </div>
        </div>

        <div class="col-span-2">
          <div class="grid grid-cols-1 sm:gap-4 gap-2">
            <h3
              class="sm:text-lg font-bold transition-colors duration-300 text-cyan-200 lg:text-gray-500 lg:group-hover:text-cyan-200"
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
                    <div
                      class="flex items-center rounded-full group-hover:bg-gray-300 group cursor-pointer bg-gray-300 lg:bg-gray-800 p-1 sm:p-2 transition-colors duration-300 lg:group-hover:bg-gray-300"
                    >
                      {#if skill.image}
                        <img
                          src={skill.image}
                          alt={skill.name}
                          class="flex w-5 h-5 sm:w-6 sm:h-6 object-contain lg:grayscale transition-all duration-300 lg:group-hover:grayscale-0"
                        />
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
  <p>{stateCtx.translation.experience?.info}</p>
{/if}
