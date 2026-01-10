<script>
  import { onMount } from 'svelte';
  import { stateCtx } from '../../store.svelte';
  import Swiper from 'swiper';
  import { Navigation, Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';

  import { Fancybox } from '@fancyapps/ui/dist/fancybox/';
  import '@fancyapps/ui/dist/fancybox/fancybox.css';

  import { Carousel } from '@fancyapps/ui/dist/carousel/';
  import '@fancyapps/ui/dist/carousel/carousel.css';

  onMount(() => {
    const swiper = new Swiper('.swiper', {
      modules: [Navigation, Pagination],
      spaceBetween: 30,
      loop: false,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });

    Fancybox.bind("[data-fancybox^='gallery-']", {
      hideScrollbar: true,
      wheel: 'slide',
      backdropClick: 'close',
      Hash: false,
    });

    const carouselInstances = Array.from(document.querySelectorAll('.f-carousel')).map((el) => {
      return Carousel(el, {
        infinite: true,
      });
    });
  });
</script>

<div class="swiper">
  <div class="swiper-wrapper">
    {#each stateCtx.projects as item}
      <div class="swiper-slide">
        <div class="grid grid-cols-{item.images.length === 0 ? '1' : '4'} gap-4 px-10">
          {#if item.images.length > 0}
            <div class="col-span-{item.images.length === 1 ? '2' : '1'} h-[350px]">
              <a href={item.images[0]} data-fancybox="gallery-{item.id}">
                <img src={item.images[0]} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
              </a>
            </div>

            {#if item.images.length > 1}
              <div class="col-span-1 flex flex-col gap-4 h-[350px] overflow-hidden">
                {#each item.images.slice(1, 4) as img}
                  <div class="flex-1 min-h-0 f-carousel__slide">
                    <a href={img} data-fancybox="gallery-{item.id}">
                      <img src={img} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
                    </a>
                  </div>
                {/each}
              </div>
            {/if}
          {/if}

          <div class="col-span-2 flex flex-col h-[350px]">
            <h3 class="text-2xl font-bold pb-2">{@html item.title}</h3>
            <div class="text-sm flex-1 overflow-y-auto">{@html item.description}</div>

            {#if item.technologies.length > 0}
              <div class="flex flex-wrap gap-2 items-center mt-4">
                {#each item.technologies as skill}
                  <div class="flex gap-2 items-center rounded-2xl px-4 py-1 bg-gray-900">
                    <img src={skill.image} alt={skill.name} title={skill.name} class="flex w-full h-6 object-cover" />

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
