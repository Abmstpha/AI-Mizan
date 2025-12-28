const withNextra = require('nextra')({
    theme: 'nextra-theme-docs',
    themeConfig: './theme.config.jsx'
})

module.exports = withNextra({
    output: 'export',
    basePath: '/AI-Mizan',
    images: {
        unoptimized: true
    }
})
