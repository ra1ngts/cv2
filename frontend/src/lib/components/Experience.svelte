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

        {#if field.skills && field.skills.length > 0}
          <div class="flex flex-row gap-4">
            {#each field.skills as skill}
              <div class="flex gap-2 items-center rounded-2xl border border-gray-800 text-gray-400 p-2">
                {#if skill.image}
                  <div>
                    <img src={skill.image} alt={skill.name} class="w-10 h-10 object-cover" />
                  </div>
                {/if}

                <div class="text-sm">
                  {skill.name}
                  <!-- {skill.level} -->
                </div>
              </div>
            {/each}
          </div>
        {/if}
      </div>
    </div>
  </a>
{/each}
