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
    const swiperProjects = new Swiper('.swiper-projects', {
      modules: [Navigation, Pagination],
      spaceBetween: 30,
      loop: false,
      pagination: {
        el: '.swiper-pagination-projects',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });

    if (stateCtx.skills && stateCtx.skills.length > 0) {
      setTimeout(() => {
        if (swiperProjects) {
          swiperProjects.update();
        }
      }, 100);
    }

    Fancybox.bind("[data-fancybox^='projects-gallery-']", {
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

<div
  class="projects pt-4 rounded-2xl transition-all duration-300 hover:bg-white/5 hover:backdrop-blur-md
        hover:shadow-2xl hover:shadow-cyan-950/20 group block"
>
  <div class="swiper swiper-projects">
    <div class="swiper-wrapper">
      {#each stateCtx.projects as item}
        <div class="swiper-slide">
          <div class="grid grid-cols-{item.images.length === 0 ? '1' : '4'} gap-4 px-10">
            {#if item.images.length > 0}
              <div class="col-span-{item.images.length === 1 ? '2' : '1'} h-80">
                <a href={item.images[0]} data-fancybox="projects-gallery-{item.id}">
                  <img src={item.images[0]} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
                </a>
              </div>

              {#if item.images.length > 1}
                <div class="col-span-1 flex flex-col gap-4 h-80 overflow-hidden">
                  {#each item.images.slice(1, 4) as img}
                    <div class="flex-1 min-h-0 f-carousel__slide">
                      <a href={img} data-fancybox="projects-gallery-{item.id}">
                        <img src={img} alt={item.title} class="w-full h-full object-cover rounded-2xl" />
                      </a>
                    </div>
                  {/each}
                </div>
              {/if}
            {/if}

            <div class="col-span-2 flex flex-col h-80">
              <div
                class="grid grid-cols-[1fr_auto_auto] py-2 items-center gap-4 [&_svg]:h-8 [&_svg]:w-8 [&_svg]:fill-gray-400 [&_svg]:hover:fill-cyan-200"
              >
                <h3 class="text-2xl font-bold transition-colors duration-300 group-hover:text-cyan-200">
                  {@html item.title}
                </h3>

                <div>
                  <a href={item.github_url} aria-label={item.github_url}>
                    <svg class="transition-colors duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                      ><path
                        d="M237.9 461.4C237.9 463.4 235.6 465 232.7 465C229.4 465.3 227.1 463.7 227.1 461.4C227.1 459.4 229.4 457.8 232.3 457.8C235.3 457.5 237.9 459.1 237.9 461.4zM206.8 456.9C206.1 458.9 208.1 461.2 211.1 461.8C213.7 462.8 216.7 461.8 217.3 459.8C217.9 457.8 216 455.5 213 454.6C210.4 453.9 207.5 454.9 206.8 456.9zM251 455.2C248.1 455.9 246.1 457.8 246.4 460.1C246.7 462.1 249.3 463.4 252.3 462.7C255.2 462 257.2 460.1 256.9 458.1C256.6 456.2 253.9 454.9 251 455.2zM316.8 72C178.1 72 72 177.3 72 316C72 426.9 141.8 521.8 241.5 555.2C254.3 557.5 258.8 549.6 258.8 543.1C258.8 536.9 258.5 502.7 258.5 481.7C258.5 481.7 188.5 496.7 173.8 451.9C173.8 451.9 162.4 422.8 146 415.3C146 415.3 123.1 399.6 147.6 399.9C147.6 399.9 172.5 401.9 186.2 425.7C208.1 464.3 244.8 453.2 259.1 446.6C261.4 430.6 267.9 419.5 275.1 412.9C219.2 406.7 162.8 398.6 162.8 302.4C162.8 274.9 170.4 261.1 186.4 243.5C183.8 237 175.3 210.2 189 175.6C209.9 169.1 258 202.6 258 202.6C278 197 299.5 194.1 320.8 194.1C342.1 194.1 363.6 197 383.6 202.6C383.6 202.6 431.7 169 452.6 175.6C466.3 210.3 457.8 237 455.2 243.5C471.2 261.2 481 275 481 302.4C481 398.9 422.1 406.6 366.2 412.9C375.4 420.8 383.2 435.8 383.2 459.3C383.2 493 382.9 534.7 382.9 542.9C382.9 549.4 387.5 557.3 400.2 555C500.2 521.8 568 426.9 568 316C568 177.3 455.5 72 316.8 72zM169.2 416.9C167.9 417.9 168.2 420.2 169.9 422.1C171.5 423.7 173.8 424.4 175.1 423.1C176.4 422.1 176.1 419.8 174.4 417.9C172.8 416.3 170.5 415.6 169.2 416.9zM158.4 408.8C157.7 410.1 158.7 411.7 160.7 412.7C162.3 413.7 164.3 413.4 165 412C165.7 410.7 164.7 409.1 162.7 408.1C160.7 407.5 159.1 407.8 158.4 408.8zM190.8 444.4C189.2 445.7 189.8 448.7 192.1 450.6C194.4 452.9 197.3 453.2 198.6 451.6C199.9 450.3 199.3 447.3 197.3 445.4C195.1 443.1 192.1 442.8 190.8 444.4zM179.4 429.7C177.8 430.7 177.8 433.3 179.4 435.6C181 437.9 183.7 438.9 185 437.9C186.6 436.6 186.6 434 185 431.7C183.6 429.4 181 428.4 179.4 429.7z"
                      /></svg
                    >
                  </a>
                </div>

                <div>
                  <a href={item.live_demo_url} aria-label={item.live_demo_url}>
                    <svg class="transition-colors duration-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                      ><path
                        d="M451.5 160C434.9 160 418.8 164.5 404.7 172.7C388.9 156.7 370.5 143.3 350.2 133.2C378.4 109.2 414.3 96 451.5 96C537.9 96 608 166 608 252.5C608 294 591.5 333.8 562.2 363.1L491.1 434.2C461.8 463.5 422 480 380.5 480C294.1 480 224 410 224 323.5C224 322 224 320.5 224.1 319C224.6 301.3 239.3 287.4 257 287.9C274.7 288.4 288.6 303.1 288.1 320.8C288.1 321.7 288.1 322.6 288.1 323.4C288.1 374.5 329.5 415.9 380.6 415.9C405.1 415.9 428.6 406.2 446 388.8L517.1 317.7C534.4 300.4 544.2 276.8 544.2 252.3C544.2 201.2 502.8 159.8 451.7 159.8zM307.2 237.3C305.3 236.5 303.4 235.4 301.7 234.2C289.1 227.7 274.7 224 259.6 224C235.1 224 211.6 233.7 194.2 251.1L123.1 322.2C105.8 339.5 96 363.1 96 387.6C96 438.7 137.4 480.1 188.5 480.1C205 480.1 221.1 475.7 235.2 467.5C251 483.5 269.4 496.9 289.8 507C261.6 530.9 225.8 544.2 188.5 544.2C102.1 544.2 32 474.2 32 387.7C32 346.2 48.5 306.4 77.8 277.1L148.9 206C178.2 176.7 218 160.2 259.5 160.2C346.1 160.2 416 230.8 416 317.1C416 318.4 416 319.7 416 321C415.6 338.7 400.9 352.6 383.2 352.2C365.5 351.8 351.6 337.1 352 319.4C352 318.6 352 317.9 352 317.1C352 283.4 334 253.8 307.2 237.5z"
                      />
                    </svg>
                  </a>
                </div>
              </div>

              <div
                class="text-sm pe-1 flex-1 overflow-y-auto scrollbar-gutter-stable
                [scrollbar-color:var(--color-gray-500)_var(--color-gray-800)]
                [scrollbar-width:thin]"
              >
                {@html item.description}
              </div>

              {#if item.technologies.length > 0}
                <div class="flex flex-wrap gap-2 items-center mt-4">
                  {#each item.technologies as skill}
                    <div
                      class="flex gap-2 items-center rounded-2xl px-4 py-1 transition-colors duration-300 group-hover:text-cyan-200 bg-gray-900 group-hover:bg-gray-800"
                    >
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

    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>

  <div class="swiper-pagination-projects"></div>
</div>
