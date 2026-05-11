# HugeiconsKMP

HugeiconsKMP is a Kotlin Multiplatform (KMP) library that brings the extensive [Hugeicons](https://hugeicons.com/) collection to your Compose Multiplatform projects. It provides high-quality SVG assets optimized for Android, iOS, and Desktop JVM targets.

## Features

- **Easy to use**: Simple `HugeIcon` composable.
- **Type-safe**: All icons are accessible via the `HugeIcons` object.
- **Multiplatform**: Supports Android, iOS, and Desktop (JVM).
- **Customizable**: Easy to change size, color, and more.

## Installation

Add the library to your shared module's `build.gradle.kts` (usually `:composeApp` or `:shared`):

```kotlin
kotlin {
    sourceSets {
        commonMain.dependencies {
            implementation("com.verimsolution:hugeiconskmp:1.0.0")
        }
    }
}
```

> **Note:** Replace `1.0.0` with the version you published or the latest available.

## Usage

### Displaying an Icon

Use the `HugeIcon` composable and choose an icon from the `HugeIcons` collection:

```kotlin
import androidx.compose.foundation.layout.size
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import com.verimsolution.hugeiconskmp.HugeIcon
import com.verimsolution.hugeiconskmp.HugeIcons

@Composable
fun MyFeature() {
    HugeIcon(
        icon = HugeIcons.Activity01Icon,
        contentDescription = "Activity Icon",
        tint = Color.Blue,
        modifier = Modifier.size(24.dp)
    )
}
```

### Direct Access

If you prefer to use the `painterResource` directly:

```kotlin
import org.jetbrains.compose.resources.painterResource
import androidx.compose.material3.Icon
import com.verimsolution.hugeiconskmp.HugeIcons

@Composable
fun DirectUsage() {
    Icon(
        painter = painterResource(HugeIcons.AlarmClockIcon),
        contentDescription = null
    )
}
```

## Local Build & Publication

### Build

```shell
./gradlew :composeApp:assembleRelease
```

### Local Publication

To use the library locally before a formal release:

```shell
./gradlew :composeApp:publishToMavenLocal
```

## Maven Central Deployment

The project is configured for Maven Central publication using the Vanniktech Gradle Maven Publish plugin.

To release a new version:
1. Ensure all secrets are configured in GitHub Actions (`MAVEN_CENTRAL_USERNAME`, `MAVEN_CENTRAL_PASSWORD`, `SIGNING_IN_MEMORY_KEY`, etc.).
2. Tag the release:
   ```shell
   git tag v1.0.0
   git push origin v1.0.0
   ```

## Project Structure

- `composeApp/src/commonMain`: Shared icons, `HugeIcon` composable, and resources.
- `composeApp/src/androidMain`: Android-specific configuration.
- `composeApp/src/iosMain`: iOS target support.
- `composeApp/src/jvmMain`: Desktop JVM target support.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
