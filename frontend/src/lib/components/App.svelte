<script>
  import { onMount } from 'svelte';
  import { stateCtx } from '../../store.svelte';
  import Profile from './Profile.svelte';
  import Experience from './Experience.svelte';
  import Projects from './Projects.svelte';

  const getCtx = async () => {
    const response = await fetch('/', {
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    if (data.status === 'success') {
      stateCtx.profile = data.profile;
      stateCtx.categories = data.categories;
      stateCtx.experience = data.experience;
      stateCtx.projects = data.projects;
      console.log('index (GET) successfully sending:', data);
    } else {
      // TODO: добавить обработку ошибок с бэка
      console.error('index (GET) sending error:', data);
    }
  };

  onMount(() => {
    getCtx();

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            stateCtx.activeSection = entry.target.id;
          }
        });
      },
      {
        rootMargin: '-40% 0px -40% 0px',
      },
    );

    stateCtx.sections.forEach((section) => {
      const el = document.getElementById(section.id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  });

  function scrollTo(id) {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>

<div class="fixed top-0 z-10 w-full bg-linear-to-b from-gray-950/80 to-gray-800/40 backdrop-blur-md px-10 py-4">
  <div class="grid grid-cols-4">
    {#each stateCtx.sections as section}
      <button
        onclick={() => scrollTo(section.id)}
        class="transition-colors duration-300 hover:text-cyan-200 text-xl font-semibold {stateCtx.activeSection ===
        section.id
          ? 'text-cyan-400'
          : 'text-gray-500'}"
      >
        {section.label}
      </button>
    {/each}
  </div>
</div>

<div class="pt-20 px-10">
  <section id="about" class="min-h-screen scroll-mt-20">
    <Profile />
  </section>

  <section id="experience" class="min-h-screen scroll-mt-20">
    <h2 class="text-4xl">Experience</h2>
    <Experience />
  </section>

  <section id="projects" class="min-h-screen scroll-mt-20">
    <h2 class="text-4xl">Projects</h2>
    <Projects />
  </section>

  <section id="contacts" class="min-h-screen scroll-mt-20">
    <h2 class="text-4xl">Contacts</h2>
  </section>
</div>
