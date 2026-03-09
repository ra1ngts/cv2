<script>
  import { stateCtx } from '../../store.svelte';
  import { getDuration } from '../../utils';
</script>

{#if stateCtx.experience.length > 0}
  {#each stateCtx.experience as entry}
    <div
      class="grid sm:grid-cols-3 mb-4 grid-cols-1 group sm:gap-4 gap-2 p-2 md:p-4 rounded-2xl transition-all duration-300 bg-white/5 shadow-2xl backdrop-blur-md hover:bg-white/5 lg:bg-transparent lg:hover:backdrop-blur-md
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
          <div class="flex justify-between w-full">
            <h3
              class="sm:text-lg font-bold transition-colors duration-300 text-cyan-200 lg:text-gray-500 lg:group-hover:text-cyan-200"
            >
              {entry.position}, {entry.company}
            </h3>

            <a
              href={entry.company_url}
              aria-label={entry.company_url}
              target="_blank"
              rel="noopener noreferrer"
              class="group block group/link"
            >
              <svg
                class="shrink-0 h-6 w-6 sm:h-7 sm:w-7 transition-colors duration-300 fill-current
                text-cyan-200 lg:text-gray-500 lg:group-hover/link:text-cyan-200"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 640 640"
              >
                <path
                  d="M451.5 160C434.9 160 418.8 164.5 404.7 172.7C388.9 156.7 370.5 143.3 350.2 133.2C378.4 109.2 414.3 96 451.5 96C537.9 96 608 166 608 252.5C608 294 591.5 333.8 562.2 363.1L491.1 434.2C461.8 463.5 422 480 380.5 480C294.1 480 224 410 224 323.5C224 322 224 320.5 224.1 319C224.6 301.3 239.3 287.4 257 287.9C274.7 288.4 288.6 303.1 288.1 320.8C288.1 321.7 288.1 322.6 288.1 323.4C288.1 374.5 329.5 415.9 380.6 415.9C405.1 415.9 428.6 406.2 446 388.8L517.1 317.7C534.4 300.4 544.2 276.8 544.2 252.3C544.2 201.2 502.8 159.8 451.7 159.8zM307.2 237.3C305.3 236.5 303.4 235.4 301.7 234.2C289.1 227.7 274.7 224 259.6 224C235.1 224 211.6 233.7 194.2 251.1L123.1 322.2C105.8 339.5 96 363.1 96 387.6C96 438.7 137.4 480.1 188.5 480.1C205 480.1 221.1 475.7 235.2 467.5C251 483.5 269.4 496.9 289.8 507C261.6 530.9 225.8 544.2 188.5 544.2C102.1 544.2 32 474.2 32 387.7C32 346.2 48.5 306.4 77.8 277.1L148.9 206C178.2 176.7 218 160.2 259.5 160.2C346.1 160.2 416 230.8 416 317.1C416 318.4 416 319.7 416 321C415.6 338.7 400.9 352.6 383.2 352.2C365.5 351.8 351.6 337.1 352 319.4C352 318.6 352 317.9 352 317.1C352 283.4 334 253.8 307.2 237.5z"
                />
              </svg>
            </a>
          </div>

          <div class="text-sm">
            {entry.achievements}
          </div>

          {#if entry.skills && entry.skills.length > 0}
            <div class="flex flex-wrap flex-row gap-2">
              {#each entry.skills as skill}
                {#if skill.category.name !== 'Certificate'}
                  <div
                    class="flex items-center rounded-full group-hover:bg-gray-300 group bg-gray-300 lg:bg-gray-800 p-1 sm:p-2 transition-colors duration-300 lg:group-hover:bg-gray-300"
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
  {/each}
{:else}
  <p>{stateCtx.translation.experience?.info}</p>
{/if}
