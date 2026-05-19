# HugeiconsKMP

HugeiconsKMP is a Kotlin Multiplatform library that brings 800+ [Hugeicons](https://hugeicons.com/) to your Compose Multiplatform projects. All icons are stroke/rounded SVG assets, optimized for Android, iOS, and Desktop (JVM).

## Features

- **Simple API**: One `HugeIcon` composable handles everything.
- **Type-safe**: All icons are accessible via the `HugeIcons` object — no string resources.
- **Multiplatform**: Android, iOS (arm64 + Simulator), Desktop JVM.
- **Customizable**: Control size, color, and anything else via `Modifier` and `tint`.

## Installation

This library is distributed via **[JitPack](https://jitpack.io)** — no authentication required.

### Step 1 — Add the JitPack repository

In your project's `settings.gradle.kts`:

```kotlin
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven { url = uri("https://jitpack.io") }
    }
}
```

### Step 2 — Add the dependency

In your shared module's `build.gradle.kts` (typically `:composeApp` or `:shared`):

```kotlin
kotlin {
    sourceSets {
        commonMain.dependencies {
            implementation("com.github.plelouch7:hugeiconskmp:1.0.0")
        }
    }
}
```

Replace `1.0.0` with the [latest release tag](https://github.com/plelouch7/KMP-Hugeicons-/releases).

## Usage

### Basic example

```kotlin
import androidx.compose.foundation.layout.size
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.verimsolution.hugeiconskmp.HugeIcon
import com.verimsolution.hugeiconskmp.HugeIcons

@Composable
fun MyScreen() {
    HugeIcon(
        icon = HugeIcons.Activity01Icon,
        contentDescription = "Activity",
        tint = Color(0xFF1A73E8),
        modifier = Modifier.size(24.dp)
    )
}
```

### Using `painterResource` directly

`HugeIcons` properties return a `DrawableResource`, so you can also use them with the standard `Icon` composable or any API that accepts a `Painter`:

```kotlin
import androidx.compose.material3.Icon
import org.jetbrains.compose.resources.painterResource
import com.verimsolution.hugeiconskmp.HugeIcons

@Composable
fun DirectUsage() {
    Icon(
        painter = painterResource(HugeIcons.AlarmClockIcon),
        contentDescription = null
    )
}
```

### Icon naming convention

All icons follow the pattern `{IconName}Icon` in PascalCase. The underlying resource files are named `{icon_name}_stroke_rounded`. Examples:

| `HugeIcons` property          | Resource file                          |
|-------------------------------|----------------------------------------|
| `HugeIcons.Activity01Icon`    | `activity_01_stroke_rounded`           |
| `HugeIcons.AlarmClockIcon`    | `alarm_clock_stroke_rounded`           |
| `HugeIcons.FirstBracketIcon`  | `_1st_bracket_stroke_rounded`          |
| `HugeIcons.AiBrain01Icon`     | `ai_brain_01_stroke_rounded`           |
| `HugeIcons.CalendarSyncIcon`  | `calendar_sync_stroke_rounded`         |

Icons that start with a number are prefixed with the written-out number (e.g., `1st` → `FirstBracketIcon`, `3d` → `ThreeDMoveIcon`).

### Tint and theming

By default, `tint = Color.Unspecified` inherits the current content color from the composition. Pass an explicit `Color` to override:

```kotlin
// Inherit from MaterialTheme
HugeIcon(icon = HugeIcons.Activity01Icon, contentDescription = null)

// Fixed tint
HugeIcon(icon = HugeIcons.Activity01Icon, contentDescription = null, tint = Color.Red)

// Theme color
HugeIcon(
    icon = HugeIcons.Activity01Icon,
    contentDescription = null,
    tint = MaterialTheme.colorScheme.primary
)
```

## Supported targets

| Target                  | Kotlin target        |
|-------------------------|----------------------|
| Android                 | `androidTarget()`    |
| iOS (device)            | `iosArm64()`         |
| iOS (Simulator)         | `iosSimulatorArm64()`|
| Desktop (JVM)           | `jvm()`              |

Minimum Android SDK: as configured in the consumer app (`minSdk` in `android {}`).

## Local build

```shell
# Publish to Maven Local for local testing
./gradlew :composeApp:publishToMavenLocal
```

Add `mavenLocal()` to your consumer project's repositories and use `com.github.plelouch7:hugeiconskmp:<version>`.

## Releasing a new version

Push a version tag — JitPack picks it up automatically and builds the library:

```shell
git tag v1.0.1
git push origin v1.0.1
```

The release will then be available at `com.github.plelouch7:hugeiconskmp:1.0.1`.

## Project structure

```
composeApp/src/
├── commonMain/   # HugeIcon composable, HugeIcons object, all XML resources
├── androidMain/  # Android-specific tooling
├── iosMain/      # iOS target entry point
└── jvmMain/      # Desktop JVM entry point
```

## License

MIT License — see the [LICENSE](LICENSE) file for details.
