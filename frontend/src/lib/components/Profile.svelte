<script>
  import { stateCtx } from '../../store.svelte';

  import Swiper from 'swiper';
  import { Navigation, Pagination, Mousewheel } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';

  import { Fancybox } from '@fancyapps/ui/dist/fancybox/';
  import '@fancyapps/ui/dist/fancybox/fancybox.css';

  import { Carousel } from '@fancyapps/ui/dist/carousel/';
  import '@fancyapps/ui/dist/carousel/carousel.css';

  let swiperSkills;

  $effect(() => {
    if (!stateCtx.certificates?.length || swiperSkills) {
      return;
    }

    swiperSkills = new Swiper('.swiper-skills', {
      modules: [Navigation, Pagination, Mousewheel],
      slidesPerView: 3,
      spaceBetween: 30,
      watchOverflow: true,
      lazyPreloadPrevNext: 1,
      loop: false,
      mousewheel: true,
      pagination: {
        el: '.swiper-pagination-skills',
        clickable: true,
      },
      navigation: {
        nextEl: '.swiper-button-next-skills',
        prevEl: '.swiper-button-prev-skills',
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 15,
          navigation: {
            enabled: false,
          },
          pagination: {
            enabled: true,
          },
        },
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
          navigation: {
            enabled: false,
          },
          pagination: {
            enabled: true,
          },
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 15,
          navigation: {
            enabled: false,
          },
          pagination: {
            enabled: true,
          },
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 15,
          navigation: {
            enabled: true,
          },
          pagination: {
            enabled: true,
          },
        },
      },
    });

    Fancybox.bind("[data-fancybox^='skills-gallery-']", {
      hideScrollbar: true,
      wheel: 'slide',
      backdropClick: 'close',
      Hash: false,
      Carousel: {
        Toolbar: {
          display: {
            left: [],
            middle: [],
            right: ['close'],
          },
        },
      },
    });

    return () => {
      swiperSkills?.destroy(true, true);

      Fancybox.unbind("[data-fancybox^='skills-gallery-']");
      Fancybox.close();
    };
  });
</script>

<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
  <div>
    <div class="flex flex-row items-stretch gap-4">
      {#if stateCtx.profile.image}
        <div class="shrink-0 hidden lg:flex items-center">
          <img
            src={stateCtx.profile.image}
            alt={stateCtx.profile.name}
            class="h-full max-h-40 object-cover aspect-square rounded-full"
            loading="eager"
            fetchpriority="high"
          />
        </div>
      {/if}

      <div class="w-fit flex flex-col justify-center gap-4">
        <div class="text-4xl sm:text-5xl gradient-to-b font-bold typing-text">
          {stateCtx.profile.name}
          {stateCtx.profile.lastname}
        </div>

        <div class="text-lg fade">
          {stateCtx.profile.occupation}
        </div>

        <div
          class="flex gap-2 items-center fill-cyan-200 [&_svg]:transition-colors [&_svg]:duration-300 [&_svg]:h-6 [&_svg]:w-6 lg:[&_svg]:fill-gray-500 lg:[&_svg]:group-hover:fill-cyan-200"
        >
          {#if stateCtx.profile.whatsapp}
            <a
              class="group"
              href={stateCtx.profile.whatsapp}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={stateCtx.profile.whatsapp}
            >
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M476.9 161.1C435 119.1 379.2 96 319.9 96C197.5 96 97.9 195.6 97.9 318C97.9 357.1 108.1 395.3 127.5 429L96 544L213.7 513.1C246.1 530.8 282.6 540.1 319.8 540.1L319.9 540.1C442.2 540.1 544 440.5 544 318.1C544 258.8 518.8 203.1 476.9 161.1zM319.9 502.7C286.7 502.7 254.2 493.8 225.9 477L219.2 473L149.4 491.3L168 423.2L163.6 416.2C145.1 386.8 135.4 352.9 135.4 318C135.4 216.3 218.2 133.5 320 133.5C369.3 133.5 415.6 152.7 450.4 187.6C485.2 222.5 506.6 268.8 506.5 318.1C506.5 419.9 421.6 502.7 319.9 502.7zM421.1 364.5C415.6 361.7 388.3 348.3 383.2 346.5C378.1 344.6 374.4 343.7 370.7 349.3C367 354.9 356.4 367.3 353.1 371.1C349.9 374.8 346.6 375.3 341.1 372.5C308.5 356.2 287.1 343.4 265.6 306.5C259.9 296.7 271.3 297.4 281.9 276.2C283.7 272.5 282.8 269.3 281.4 266.5C280 263.7 268.9 236.4 264.3 225.3C259.8 214.5 255.2 216 251.8 215.8C248.6 215.6 244.9 215.6 241.2 215.6C237.5 215.6 231.5 217 226.4 222.5C221.3 228.1 207 241.5 207 268.8C207 296.1 226.9 322.5 229.6 326.2C232.4 329.9 268.7 385.9 324.4 410C359.6 425.2 373.4 426.5 391 423.9C401.7 422.3 423.8 410.5 428.4 397.5C433 384.5 433 373.4 431.6 371.1C430.3 368.6 426.6 367.2 421.1 364.5z"
                  /></svg
                >
              </div>
            </a>
          {/if}

          {#if stateCtx.profile.telegram}
            <a
              class="group"
              href={stateCtx.profile.telegram}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={stateCtx.profile.telegram}
            >
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M320 72C183 72 72 183 72 320C72 457 183 568 320 568C457 568 568 457 568 320C568 183 457 72 320 72zM435 240.7C431.3 279.9 415.1 375.1 406.9 419C403.4 437.6 396.6 443.8 390 444.4C375.6 445.7 364.7 434.9 350.7 425.7C328.9 411.4 316.5 402.5 295.4 388.5C270.9 372.4 286.8 363.5 300.7 349C304.4 345.2 367.8 287.5 369 282.3C369.2 281.6 369.3 279.2 367.8 277.9C366.3 276.6 364.2 277.1 362.7 277.4C360.5 277.9 325.6 300.9 258.1 346.5C248.2 353.3 239.2 356.6 231.2 356.4C222.3 356.2 205.3 351.4 192.6 347.3C177.1 342.3 164.7 339.6 165.8 331C166.4 326.5 172.5 322 184.2 317.3C256.5 285.8 304.7 265 328.8 255C397.7 226.4 412 221.4 421.3 221.2C423.4 221.2 427.9 221.7 430.9 224.1C432.9 225.8 434.1 228.2 434.4 230.8C434.9 234 435 237.3 434.8 240.6z"
                  /></svg
                >
              </div>
            </a>
          {/if}

          {#if stateCtx.profile.linkedin}
            <a
              class="group"
              href={stateCtx.profile.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={stateCtx.profile.linkedin}
            >
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M160 96C124.7 96 96 124.7 96 160L96 480C96 515.3 124.7 544 160 544L480 544C515.3 544 544 515.3 544 480L544 160C544 124.7 515.3 96 480 96L160 96zM165 266.2L231.5 266.2L231.5 480L165 480L165 266.2zM236.7 198.5C236.7 219.8 219.5 237 198.2 237C176.9 237 159.7 219.8 159.7 198.5C159.7 177.2 176.9 160 198.2 160C219.5 160 236.7 177.2 236.7 198.5zM413.9 480L413.9 376C413.9 351.2 413.4 319.3 379.4 319.3C344.8 319.3 339.5 346.3 339.5 374.2L339.5 480L273.1 480L273.1 266.2L336.8 266.2L336.8 295.4L337.7 295.4C346.6 278.6 368.3 260.9 400.6 260.9C467.8 260.9 480.3 305.2 480.3 362.8L480.3 480L413.9 480z"
                  /></svg
                >
              </div>
            </a>
          {/if}

          {#if stateCtx.profile.github}
            <a
              class="group"
              href={stateCtx.profile.github}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={stateCtx.profile.github}
            >
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M237.9 461.4C237.9 463.4 235.6 465 232.7 465C229.4 465.3 227.1 463.7 227.1 461.4C227.1 459.4 229.4 457.8 232.3 457.8C235.3 457.5 237.9 459.1 237.9 461.4zM206.8 456.9C206.1 458.9 208.1 461.2 211.1 461.8C213.7 462.8 216.7 461.8 217.3 459.8C217.9 457.8 216 455.5 213 454.6C210.4 453.9 207.5 454.9 206.8 456.9zM251 455.2C248.1 455.9 246.1 457.8 246.4 460.1C246.7 462.1 249.3 463.4 252.3 462.7C255.2 462 257.2 460.1 256.9 458.1C256.6 456.2 253.9 454.9 251 455.2zM316.8 72C178.1 72 72 177.3 72 316C72 426.9 141.8 521.8 241.5 555.2C254.3 557.5 258.8 549.6 258.8 543.1C258.8 536.9 258.5 502.7 258.5 481.7C258.5 481.7 188.5 496.7 173.8 451.9C173.8 451.9 162.4 422.8 146 415.3C146 415.3 123.1 399.6 147.6 399.9C147.6 399.9 172.5 401.9 186.2 425.7C208.1 464.3 244.8 453.2 259.1 446.6C261.4 430.6 267.9 419.5 275.1 412.9C219.2 406.7 162.8 398.6 162.8 302.4C162.8 274.9 170.4 261.1 186.4 243.5C183.8 237 175.3 210.2 189 175.6C209.9 169.1 258 202.6 258 202.6C278 197 299.5 194.1 320.8 194.1C342.1 194.1 363.6 197 383.6 202.6C383.6 202.6 431.7 169 452.6 175.6C466.3 210.3 457.8 237 455.2 243.5C471.2 261.2 481 275 481 302.4C481 398.9 422.1 406.6 366.2 412.9C375.4 420.8 383.2 435.8 383.2 459.3C383.2 493 382.9 534.7 382.9 542.9C382.9 549.4 387.5 557.3 400.2 555C500.2 521.8 568 426.9 568 316C568 177.3 455.5 72 316.8 72zM169.2 416.9C167.9 417.9 168.2 420.2 169.9 422.1C171.5 423.7 173.8 424.4 175.1 423.1C176.4 422.1 176.1 419.8 174.4 417.9C172.8 416.3 170.5 415.6 169.2 416.9zM158.4 408.8C157.7 410.1 158.7 411.7 160.7 412.7C162.3 413.7 164.3 413.4 165 412C165.7 410.7 164.7 409.1 162.7 408.1C160.7 407.5 159.1 407.8 158.4 408.8zM190.8 444.4C189.2 445.7 189.8 448.7 192.1 450.6C194.4 452.9 197.3 453.2 198.6 451.6C199.9 450.3 199.3 447.3 197.3 445.4C195.1 443.1 192.1 442.8 190.8 444.4zM179.4 429.7C177.8 430.7 177.8 433.3 179.4 435.6C181 437.9 183.7 438.9 185 437.9C186.6 436.6 186.6 434 185 431.7C183.6 429.4 181 428.4 179.4 429.7z"
                  /></svg
                >
              </div>
            </a>
          {/if}

          {#if stateCtx.profile.email}
            <a class="group" href="mailto:{stateCtx.profile.email}" aria-label="Mail to: {stateCtx.profile.email}">
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M320 128C214 128 128 214 128 320C128 426 214 512 320 512C337.7 512 352 526.3 352 544C352 561.7 337.7 576 320 576C178.6 576 64 461.4 64 320C64 178.6 178.6 64 320 64C461.4 64 576 178.6 576 320L576 352C576 405 533 448 480 448C450.7 448 424.4 434.8 406.8 414.1C384 435.1 353.5 448 320 448C249.3 448 192 390.7 192 320C192 249.3 249.3 192 320 192C347.9 192 373.7 200.9 394.7 216.1C400.4 211.1 407.8 208 416 208C433.7 208 448 222.3 448 240L448 352C448 369.7 462.3 384 480 384C497.7 384 512 369.7 512 352L512 320C512 214 426 128 320 128zM384 320C384 284.7 355.3 256 320 256C284.7 256 256 284.7 256 320C256 355.3 284.7 384 320 384C355.3 384 384 355.3 384 320z"
                  /></svg
                >
              </div>
            </a>
          {/if}

          {#if stateCtx.profile.cv}
            <a
              class="group"
              href={stateCtx.profile.cv}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={stateCtx.profile.cv}
            >
              <div class="rounded-full bg-gray-800 p-1 sm:p-2 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"
                  ><path
                    d="M304 112L192 112C183.2 112 176 119.2 176 128L176 512C176 520.8 183.2 528 192 528L448 528C456.8 528 464 520.8 464 512L464 272L376 272C336.2 272 304 239.8 304 200L304 112zM444.1 224L352 131.9L352 200C352 213.3 362.7 224 376 224L444.1 224zM128 128C128 92.7 156.7 64 192 64L325.5 64C342.5 64 358.8 70.7 370.8 82.7L493.3 205.3C505.3 217.3 512 233.6 512 250.6L512 512C512 547.3 483.3 576 448 576L192 576C156.7 576 128 547.3 128 512L128 128z"
                  /></svg
                >
              </div>
            </a>
          {/if}
        </div>
      </div>
    </div>

    <h2 class="pt-4 sm:pt-8 pb-2 sm:pb-4 text-xl sm:text-2xl font-bold">
      {stateCtx.translation.profile?.technologies}
    </h2>
    <hr class="py-2 border-gray-500/50 opacity-50" />

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 sm:gap-4">
      <div class="flex flex-col">
        <h3 class="pb-2 sm:pb-4">{stateCtx.translation.profile?.frontend}</h3>

        <div class="flex flex-wrap gap-2 group">
          {#each stateCtx.frontendSkills as skill}
            <div
              class="rounded-full p-1 sm:p-2 transition-colors duration-300 bg-gray-300 lg:bg-gray-800 lg:group-hover:bg-gray-300 group"
            >
              <img
                src={skill.image}
                alt={skill.name}
                class="w-5 h-5 sm:w-6 sm:h-6 object-contain transition-all duration-300 lg:grayscale lg:group-hover:grayscale-0"
                loading="lazy"
              />
            </div>
          {/each}
        </div>
      </div>

      <div class="flex flex-col">
        <h3 class="pb-2 sm:pb-4">{stateCtx.translation.profile?.backend}</h3>

        <div class="flex flex-wrap gap-2 group">
          {#each stateCtx.backendSkills as skill}
            <div
              class="rounded-full p-1 sm:p-2 transition-colors duration-300 bg-gray-300 lg:bg-gray-800 lg:group-hover:bg-gray-300 group"
            >
              <img
                src={skill.image}
                alt={skill.name}
                class="w-5 h-5 sm:w-6 sm:h-6 object-contain transition-all duration-300 lg:grayscale lg:group-hover:grayscale-0"
                loading="lazy"
              />
            </div>
          {/each}
        </div>
      </div>

      <div class="flex flex-col">
        <h3 class="pb-2 sm:pb-4">{stateCtx.translation.profile?.tools}</h3>

        <div class="flex flex-wrap gap-2 group">
          {#each stateCtx.tools as skill}
            <div
              class="rounded-full p-1 sm:p-2 transition-colors duration-300 bg-gray-300 lg:bg-gray-800 lg:group-hover:bg-gray-300 group"
            >
              <img
                src={skill.image}
                alt={skill.name}
                class="w-5 h-5 sm:w-6 sm:h-6 object-contain transition-all duration-300 lg:grayscale lg:group-hover:grayscale-0"
                loading="lazy"
              />
            </div>
          {/each}
        </div>
      </div>
    </div>
  </div>

  <div>
    {@html stateCtx.profile.description}
  </div>
</div>

{#if stateCtx.certificates.length > 0}
  <div class="skills mt-5 sm:mt-10 pt-4">
    <div class="swiper swiper-skills min-h-100">
      <div class="swiper-wrapper">
        {#each stateCtx.certificates as skill}
          <div class="swiper-slide h-auto! flex">
            <div
              class="group h-full flex flex-col gap-4 px-4 lg:px-10 py-4 rounded-3xl transition-all duration-300 bg-white/5 shadow-2xl backdrop-blur-md hover:bg-white/5 lg:bg-transparent lg:hover:backdrop-blur-md
                lg:hover:shadow-2xl lg:hover:shadow-cyan-950/20"
            >
              <div class="h-64 overflow-hidden rounded-2xl bg-white">
                <a
                  class="relative block w-full h-full overflow-hidden"
                  href={skill.image}
                  data-fancybox="skills-gallery-{skill.id}"
                >
                  <img
                    src={skill.image}
                    alt={skill.name}
                    class="w-full h-full object-contain cursor-pointer opacity-100 lg:opacity-90 lg:group-hover:opacity-100 transition-opacity duration-300"
                    loading="lazy"
                  />
                  <div class="swiper-lazy-preloader"></div>
                </a>
              </div>

              <div
                class="grid grid-cols-[1fr_auto_auto] py-2 [&_svg]:h-6 [&_svg]:w-6 sm:[&_svg]:h-7 sm:[&_svg]:w-7 [&_svg]:fill-cyan-200 lg:[&_svg]:fill-gray-500 lg:[&_svg]:hover:fill-cyan-200"
              >
                {#if skill.skill_url}
                  <div
                    class="sm:text-md font-bold transition-colors duration-300 text-cyan-200 lg:text-gray-500 lg:group-hover:text-cyan-200"
                  >
                    {skill.name}
                  </div>
                  <a
                    href={skill.skill_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    aria-label={skill.skill_url}
                    class="flex w-full justify-between items-center group/link ps-2"
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
                {:else}
                  <div
                    class="text-md justify-center transition-colors duration-300 text-cyan-200 lg:text-gray-500 lg:group-hover:text-cyan-200"
                  >
                    {skill.name}
                  </div>
                {/if}
              </div>
            </div>
          </div>
        {/each}
      </div>

      <div class="swiper-button-prev swiper-button-prev-skills"></div>
      <div class="swiper-button-next swiper-button-next-skills"></div>
    </div>

    <div class="swiper-pagination-skills"></div>
  </div>
{:else}
  <p>{stateCtx.translation.profile?.info}</p>
{/if}
