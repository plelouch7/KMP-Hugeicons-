import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.gradle.plugins.signing.SigningExtension

plugins {
    alias(libs.plugins.kotlinMultiplatform)
    alias(libs.plugins.androidLibrary)
    alias(libs.plugins.composeMultiplatform)
    alias(libs.plugins.composeCompiler)
    alias(libs.plugins.mavenPublish)
}

base {
    archivesName.set("hugeiconskmp")
}

compose.resources {
    packageOfResClass = "com.verimsolution.hugeiconskmp.generated.resources"
    publicResClass = true
}

publishing {
    val remoteMavenUrl = providers.gradleProperty("remoteMavenUrl")
        .orElse(providers.environmentVariable("REMOTE_MAVEN_URL"))
    val remoteMavenUsername = providers.gradleProperty("remoteMavenUsername")
        .orElse(providers.environmentVariable("REMOTE_MAVEN_USERNAME"))
    val remoteMavenPassword = providers.gradleProperty("remoteMavenPassword")
        .orElse(providers.environmentVariable("REMOTE_MAVEN_PASSWORD"))

    repositories {
        if (remoteMavenUrl.isPresent) {
            maven {
                name = "remote"
                url = uri(remoteMavenUrl.get())
                credentials {
                    username = remoteMavenUsername.orNull
                    password = remoteMavenPassword.orNull
                }
            }
        }
    }
}

mavenPublishing {
    publishToMavenCentral()
    signAllPublications()
}

extensions.configure<SigningExtension>("signing") {
    val publishingToMavenCentral = gradle.startParameter.taskNames.any {
        it.contains("MavenCentral", ignoreCase = true)
    }
    isRequired = publishingToMavenCentral
}

kotlin {
    androidTarget {
        compilerOptions {
            jvmTarget.set(JvmTarget.JVM_11)
        }
        publishLibraryVariants("release")
    }
    
    listOf(
        iosArm64(),
        iosSimulatorArm64()
    ).forEach { iosTarget ->
        iosTarget.binaries.framework {
            baseName = "HugeiconsKMP"
            isStatic = true
        }
    }
    
    jvm()
    
    sourceSets {
        androidMain.dependencies {
            implementation(libs.compose.uiToolingPreview)
        }
        commonMain.dependencies {
            api(libs.compose.runtime)
            api(libs.compose.foundation)
            api(libs.compose.material3)
            api(libs.compose.ui)
            api(libs.compose.components.resources)
            api(libs.compose.uiToolingPreview)
            api(libs.androidx.lifecycle.viewmodelCompose)
            api(libs.androidx.lifecycle.runtimeCompose)
        }
        commonTest.dependencies {
            implementation(libs.kotlin.test)
        }
    }
}

android {
    namespace = "com.verimsolution.hugeiconskmp"
    compileSdk = libs.versions.android.compileSdk.get().toInt()

    defaultConfig {
        minSdk = libs.versions.android.minSdk.get().toInt()
    }
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
    buildTypes {
        getByName("release") {
            isMinifyEnabled = false
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
}

dependencies {
    debugImplementation(libs.compose.uiTooling)
}
