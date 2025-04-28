<script>
  import NavBar from '$lib/components/NavBar.svelte';
  import SpotifyStatus from '$lib/components/SpotifyStatus.svelte';
  import Status from '$lib/components/Status.svelte';
  import BDay from '$lib/components/BDay.svelte'
</script>

<NavBar />

<main class="text-white min-h-screen py-10">
  <div class="max-w-4xl mx-auto px-6">
    <header class="text-left">
      <h1 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r text-white mb-4 mt-[75px]">
        Hey I'm Joshua
      </h1>
      <a aria-hidden="true" target="_blank" href="https://go.joshua.moe/github">Github</a>
      <a aria-hidden="true" target="_blank" href="https://go.joshua.moe/discord">Discord</a>
      <a aria-hidden="true" target="_blank" href="https://go.joshua.moe/anilist">Anlist</a>
      <a aria-hidden="true" href="mailto:hello@joshua.moe">Email</a>

      <p class="text-2xl font-semibold text-white pt-[10px]">Who Am I?</p>
      <p class="text-gray-300 mb-6 pt-[10px]">
        Hey, I'm Joshua or rather known online as Mobetsu. I'm a <BDay /> year old idiot who loves to watch anime, play Minecraft, program, and to self-host. I also love discussing these topics with people.
        <span class="inline-block ml-2">
          <Status />
        </span>
      </p>
    </header>

    <section class="mt-8 text-left">
      <h2 class="text-2xl font-semibold text-white">Music</h2>
      
      <div class="pl-0 -ml-6">
        <div> <!-- class="max-w-lg" if you want it to be short -->
          <SpotifyStatus />
        </div>
      </div>
    </section>

    <section class="mt-8 text-left">
      <h2 class="text-2xl font-semibold text-white">My Projects</h2>
      <ul class="mt-4 space-y-2">
        <li class="text-lg text-gray-300 flex items-center justify-between">
          <span>Pokedex bot</span>
          <div class="flex-grow border-t border-gray-500 mx-4"></div>
          <span class="text-sm text-gray-500">Founder/Dev</span>
        </li>
        <li class="text-lg text-gray-300 flex items-center justify-between">
          <span>Shigeo - My personal Discord bot</span>
          <div class="flex-grow border-t border-gray-500 mx-4"></div>
          <span class="text-sm text-gray-500">Founder/Dev</span>
        </li>
        <li class="text-lg text-gray-300 flex items-center justify-between">
          <span>Joshua.moe</span>
          <div class="flex-grow border-t border-gray-500 mx-4"></div>
          <span class="text-sm text-gray-500">Dev</span>
        </li>
      </ul>
    </section>
  </div>
</main>
