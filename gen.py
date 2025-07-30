import tomllib


INPUT_FILE = 'hayatmojis.toml'
OUTPUT_FILE = 'dist/index.html'

HTML_HEADER = '''<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>hayatmoji | An emoji guide for my commit messages</title>
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <meta name="description" content="An emoji guide for my commit messages" />

  <meta property="og:url" content="https://moji.hayatro.id" />
  <meta property="og:title" content="hayatmoji" />
  <meta property="og:type" content="website" />
  <meta property="og:description" content="An emoji guide for my commit messages" />
  <meta property="og:image" content="https://moji.hayatro.id/ogp.png" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:site" content="@hayatroid" />

  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  <script src="https://cdn.jsdelivr.net/npm/clipboard@2/dist/clipboard.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.css">
  <script src="https://cdn.jsdelivr.net/npm/notyf@3/notyf.min.js"></script>

  <style type="text/tailwindcss">
    @theme {
      --animate-wiggle: wiggle .5s;

      @keyframes wiggle {
        0%, 20%, 53%, 80%, to {
          animation-timing-function: cubic-bezier(.215, .61, .355, 1);
          transform: translateZ(0);
        }
        40%, 43% {
          animation-timing-function: cubic-bezier(.755, .05, .855, .06);
          transform: translate3d(0, -9px, 0);
        }
        70% {
          animation-timing-function: cubic-bezier(.755, .05, .855, .06);
          transform: translate3d(0, -5px, 0);
        }
        90% {
          transform: translate3d(0, -2px, 0);
        }
      }
    }
  </style>
</head>

<body>
  <header class="px-8 py-16 bg-amber-300">
    <div class="text-center flex flex-col gap-8">
      <h1 class="text-[min(14vw,6rem)] font-bold">hayatm🫣ji</h1>
      <p class="text-3xl font-bold">An emoji guide for my commit messages</p>
      <div class="flex justify-center gap-4">
        <a href="https://github.com/hayatroid/hayatmoji"
          class="p-4 rounded text-white text-lg font-bold cursor-pointer bg-rose-400 shadow-rose-600 shadow-[0_4px_0_0] hover:shadow-[0_2px_0_0] hover:translate-y-[2px]">
          ⭐ GitHub
        </a>
        <a target="_blank"
          href="https://twitter.com/intent/tweet?text=hayatmoji%20%E2%80%93%20An%20%23emoji%20guide%20for%20my%20commit%20messages%20by%20%40hayatroid%20%F0%9F%AB%A3%F0%9F%A4%A6%20https%3A%2F%2Fmoji.hayatro.id"
          class="p-4 rounded text-white text-lg font-bold cursor-pointer bg-rose-400 shadow-rose-600 shadow-[0_4px_0_0] hover:shadow-[0_2px_0_0] hover:translate-y-[2px]">
          𝕏 Share
        </a>
      </div>
    </div>
  </header>

  <main class="px-8 py-16">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
'''

HTML_CARD = '''
      <div class="rounded-lg overflow-hidden shadow-sm hover:shadow-xl transition-shadow">
        <div class="p-8 flex items-center justify-center {background}">
          <button class="text-8xl cursor-pointer hover:animate-wiggle" data-clipboard-text="{emoji}">
            {emoji}
          </button>
        </div>
        <div class="p-8 flex flex-col gap-4 text-center">
          <button class="text-xl font-bold cursor-pointer hover:animate-wiggle" data-clipboard-text="{code}">
            {code_with_wbr}
          </button>
          <p class="text-gray-400">{description}</p>
        </div>
      </div>
'''

HTML_FOOTER = '''
    </div>
  </main>

  <footer class="px-8 py-12 bg-cyan-300">
    <div class="max-w-6xl mx-auto flex justify-between gap-4 text-white text-xl font-bold">
      <div class="flex gap-2">
        <span>Made with 🤦 by </span>
        <a href="https://github.com/hayatroid" class="text-red-500 hover:animate-wiggle">hayatroid</a>
      </div>
      <a href="https://github.com/hayatroid/hayatmoji" class="text-red-500 hover:animate-wiggle">GitHub</a>
    </div>
  </footer>

  <script>
    const notyf = new Notyf();
    const clipboard = new ClipboardJS('[data-clipboard-text]');
    clipboard.on('success', (e) => {
      notyf.success(`Hey! Hayatmoji ${e.text} copied to the clipboard 🫣`);
    });
  </script>
</body>

</html>
'''


def with_wbr(code):
    parts = [f'<span>{part}</span>' for part in code.split('_')]
    return '<span>_<wbr></span>'.join(parts)


def main():
    with open(INPUT_FILE, 'rb') as toml_file:
        toml_data = tomllib.load(toml_file)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as html_file:
        html_file.write(HTML_HEADER)

        for key, info in toml_data['hayatmojis'].items():
            code = f':{key}:'
            code_with_wbr = with_wbr(code)

            card = HTML_CARD.format(
                emoji=info['emoji'],
                background=info['background'],
                code=code,
                code_with_wbr=code_with_wbr,
                description=info['description']
            )
            html_file.write(card)

        html_file.write(HTML_FOOTER)

    print(f"{OUTPUT_FILE} generated successfully!")


if __name__ == '__main__':
    main()
