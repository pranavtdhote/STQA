package com.demo;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.OutputType;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;
import java.time.Duration;

public class App {

    // Screenshot Method
    public static void takeScreenshot(WebDriver driver, String name) {

        try {

            File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);

            File dest = new File("D:\\Testing\\Screenshots\\" + name + ".png");

            dest.getParentFile().mkdirs();

            Files.copy(src.toPath(), dest.toPath(),
                    StandardCopyOption.REPLACE_EXISTING);

            System.out.println("Screenshot Taken: " + name);

        }

        catch (IOException e) {

            System.out.println("Screenshot Failed");

        }

    }


    public static void main(String[] args) {

        WebDriver driver = null;

        boolean testPassed = true;

        try {

            System.out.println("===== TEST STARTED =====");


            // STEP 1: Launch Browser

            driver = new ChromeDriver();

            driver.manage().window().maximize();

            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

            System.out.println("STEP 1: Browser Launched");

            takeScreenshot(driver,"Step1_Browser");


            // STEP 2: Open Website

            driver.get("https://www.saucedemo.com");

            System.out.println("STEP 2: Website Opened");

            takeScreenshot(driver,"Step2_Website");


            // STEP 3: Enter Username

            WebElement username = driver.findElement(By.id("user-name"));

            username.sendKeys("standard_user");

            System.out.println("STEP 3: Username Entered");



            // STEP 4: Enter Password

            WebElement password = driver.findElement(By.id("password"));

            password.sendKeys("secret_sauce");

            System.out.println("STEP 4: Password Entered");

            takeScreenshot(driver,"Step4_LoginDetails");



            // STEP 5: Click Login

            driver.findElement(By.id("login-button")).click();

            System.out.println("STEP 5: Login Clicked");

            takeScreenshot(driver,"Step5_LoginSuccess");



            // STEP 6: Verify Login

            String title = driver.getTitle();

            if(title.contains("Swag")) {

                System.out.println("STEP 6: Login Successful");

            }

            else {

                System.out.println("STEP 6: Login Failed");

                testPassed=false;

            }



            // STEP 7: Add Product to Cart

            driver.findElement(By.id("add-to-cart-sauce-labs-backpack")).click();

            System.out.println("STEP 7: Product Added");

            takeScreenshot(driver,"Step7_ProductAdded");



        }


        catch(Exception e){

            testPassed=false;

            System.out.println("Error: "+e.getMessage());

        }


        finally {

            driver.quit();

            System.out.println("Browser Closed");

            System.out.println("===== FINAL RESULT =====");


            if(testPassed)

                System.out.println("TEST RESULT: PASS");

            else

                System.out.println("TEST RESULT: FAIL");

        }

    }

}