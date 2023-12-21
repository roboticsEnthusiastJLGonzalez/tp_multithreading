#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <Eigen/Dense>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

class Task
{
private:
    int identifier;
    int size;
    Eigen::MatrixXd matrixA;
    Eigen::VectorXd matrixB;
    Eigen::VectorXd matrixX;
    long time;

public:
    Task(nlohmann::json json_task)
    {
        Eigen::MatrixXd matrixA(json_task.at("a").size(), json_task.at("a")[0].size());
        for (int i = 0; i < matrixA.rows(); ++i)
        {
            for (int j = 0; j < matrixA.cols(); ++j)
            {
                matrixA(i, j) = json_task.at("a")[i][j];
            }
        }
        this->matrixA = matrixA;

        Eigen::VectorXd matrixB(json_task.at("b").size());
        for (int i = 0; i < matrixB.size(); ++i)
        {
            matrixB(i) = json_task.at("b")[i];
        }
        this->matrixB = matrixB;
    }

    double work()
    {
        const auto time_start = std::chrono::high_resolution_clock::now();
        // too slow but super accurate
        // this->matrixX = this->matrixA.fullPivLu().solve(this->matrixB);

        // less slow and accurate
        // this->matrixX = this->matrixA.colPivHouseholderQr().solve(this->matrixB);

        // fast! but does not work (probably because the matix is not definie positive)
        // this->matrixX = this->matrixA.llt().solve(this->matrixB);

        // pretty fast and accurate and works!
        // this->matrixX = this->matrixA.householderQr().solve(this->matrixB);

        // this one can use internal multithreading
        // this->matrixX = this->matrixA.partialPivLu().solve(this->matrixB);

        // pour comparer avec résultats du prof
        this->matrixX = this->matrixA.lu().solve(this->matrixB);
        /* RESULTS
        pour 1 thread : Resolution error : 2.36743e-11
                        Execution time: 1.66699 seconds
        pour 2 threads: Resolution error : 2.22848e-10
                        Execution time: 1.02086 seconds
        pour 4 threads: Resolution error : 7.64654e-11
                        Execution time: 0.842575 seconds*/

        const auto time_end = std::chrono::high_resolution_clock::now();
        auto time_ellapsed = std::chrono::duration_cast<std::chrono::duration<double>>(time_end - time_start).count();

        // verification
        const Eigen::MatrixXd result_matrix = this->matrixA * this->matrixX - this->matrixB;
        std::cout << "Resolution error : " << result_matrix.norm() << '\n';

        return time_ellapsed;
    }
};

int main()
{
    // choix du nombre de threads utilisés lors du calcul de eigen
    Eigen::setNbThreads(4);

    // get json text from an http request
    // will wait until a response arrives
    const cpr::Response response = cpr::Get(cpr::Url{"http://localhost:8000/"});

    if (response.status_code != 200) // 200 is code for connection sucess
    {
        std::cout << "ERROR : couldn't get a correct response" << '\n';
        std::cout << "error code: " << response.status_code << "\n";
    }
    else
    {
        // create a json object to get info from it
        const auto json_task = nlohmann::json::parse(response.text);
        // std::cout << "TASK : " << json_task.at("id") << '\n';
        // std::cout << "size : " << json_task.at("size") << '\n';
        // std::cout << "size : " << json_task.at("a") << '\n';
        Task task(json_task);
        const double executionTime = task.work();
        std::cout << "Execution time: " << executionTime << " seconds" << std::endl;
    }

    return 0;
}
