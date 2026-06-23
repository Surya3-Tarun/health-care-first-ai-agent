$secret = 'GROQ_API_KEY=YOUR_API_KEY'
$replacement = 'GROQ_API_KEY=your_key_here'

$envFiles = @('.env', '.env.local', '.env.production', '.env.development')
foreach ($file in $envFiles) {
    if (Test-Path $file) {
        Remove-Item -Force $file -ErrorAction SilentlyContinue
    }
}

if (Test-Path '.env.example') {
    $content = Get-Content '.env.example' -Raw
    $newContent = $content -replace [regex]::Escape($secret), $replacement
    if ($newContent -ne $content) {
        Set-Content '.env.example' -Value $newContent
    }
}

if (Test-Path 'DEBUG_FIXES.md') {
    $content = Get-Content 'DEBUG_FIXES.md' -Raw
    $newContent = $content -replace [regex]::Escape($secret), $replacement
    if ($newContent -ne $content) {
        Set-Content 'DEBUG_FIXES.md' -Value $newContent
    }
}
