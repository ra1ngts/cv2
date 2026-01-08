<script>
  import { onMount } from 'svelte';
  import { stateCtx } from '../../store.svelte';
  import Swiper from 'swiper';
  import { Navigation, Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';

  onMount(() => {
    const swiper = new Swiper('.swiper', {
      modules: [Navigation, Pagination],
      slidesPerView: 1,
      spaceBetween: 30,
      loop: false,
      autoHeight: false,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      breakpoints: {
        1024: { slidesPerView: 1 },
      },
    });
  });
</script>

<div class="swiper">
  <div class="swiper-wrapper">
    {#each stateCtx.projects as item}
      <div class="swiper-slide">
        <div class="grid grid-cols-4 gap-4 px-10">
          <div class="col-span-1 h-[350px]">
            <img src={item.main_image} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
          </div>

          <div class="col-span-1 flex flex-col gap-4 h-[350px] overflow-hidden">
            {#each item.images.slice(0, 3) as img}
              <div class="flex-1 min-h-0">
                <img src={img} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
              </div>
            {/each}
          </div>

          <div class="col-span-2 flex flex-col h-[350px]">
            <h3 class="text-2xl font-bold pb-2">{@html item.title}</h3>
            <div class="text-sm flex-1 overflow-y-auto">{@html item.description}</div>

            {#if item.technologies.length > 0}
              <div class="flex gap-2 items-center mt-4">
                {#each item.technologies as skill}
                  <div class="flex gap-2 items-center rounded-2xl px-4 py-1 bg-gray-900">
                    <img src={skill.image} alt={skill.name} title={skill.name} class="flex w-10 h-10 object-cover" />

                    <div class="text-sm font-semibold">
                      {skill.name}
                    </div>
                  </div>
                {/each}
              </div>
            {/if}
          </div>
        </div>
      </div>
    {/each}
  </div>

  <div class="swiper-pagination"></div>

  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
